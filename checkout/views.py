# Import required modules and classes from Django
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

# Import required local modules
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Print
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from basket.contexts import basket_contents

import stripe # Import stripe payment system for handling payments
import json # For storing the basket


@require_POST
def cache_checkout_data(request):
    """ Cache the checkout data to be used with Stripe PaymentIntent """

    try:
        # Get the PaymentIntent ID from the client secret (needed for modifying the payment intent)
        pid = request.POST.get('client_secret').split('_secret')[0]

        # Set the Stripe API key for authentication
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Modify the PaymentIntent to attach additional metadata (basket info, user info, etc.)
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),  # Serialize the basket to JSON
            'save_info': request.POST.get('save_info'),  # Whether the user opted to save their info
            'username': request.user,  # Attach the username (current logged-in user)
        })

        return HttpResponse(status=200)  # Return a successful response if the operation is successful

    except Exception as e:
        # If any error occurs, show an error message and return a 400 HTTP response with the error content
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ View to render the checkout page where users can review and submit their order """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY  # Get the Stripe public key for client-side integration
    stripe_secret_key = settings.STRIPE_SECRET_KEY  # Get the Stripe secret key for server-side integration

    if request.method == 'POST':  # Handle form submission when the user submits their checkout details

        # Get the basket from the session (the items the user has added to the basket)
        basket = request.session.get('basket', {})

        # Prepare the form data from the POST request
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Instantiate the order form with the form data
        order_form = OrderForm(form_data)

        # If the form is valid, proceed to create the order
        if order_form.is_valid():
            order = order_form.save(commit=False)  # Create order object but don't save yet
            pid = request.POST.get('client_secret').split('_secret')[0]  # Get the PaymentIntent ID
            order.stripe_pid = pid  # Store the Stripe PaymentIntent ID with the order
            order.original_basket = json.dumps(basket)  # Store the original basket as JSON
            order.save()  # Save the order to the database

            # Loop through each item in the basket and create an order line item
            for item_id, item_data in basket.items():
                try:
                    product = Print.objects.get(id=item_id)  # Retrieve the product from the database
                    if isinstance(item_data, int):  # If the item is a single quantity
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()  # Save the order line item

                    else:  # If the item data is a dictionary (in case of variant items with multiple quantities)
                        for quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()

                except Print.DoesNotExist:
                    # If a product does not exist, show an error message and delete the order
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()  # Delete the order if a product is missing
                    return redirect(reverse('view_basket'))  # Redirect to the basket view

            # Store whether the user wants to save their info for future orders
            request.session['save_info'] = 'save-info' in request.POST

            # Redirect to the success page with the order number
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            # If the form is not valid, show an error message
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:  # If it's a GET request, display the checkout page with pre-filled data
        basket = request.session.get('basket', {})

        # Prevent users from accessing the checkout page if their basket is empty
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))  # Redirect to the products page

        # Get the basket details and calculate the total cost
        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)  # Stripe expects the total in cents, so we multiply by 100

        # Create a PaymentIntent with Stripe to initiate the payment process
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # If the user is authenticated (logged in), try to pre-fill the form with the user's profile data
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()  # If the profile doesn't exist, just show a blank form
        else:
            order_form = OrderForm()  # Show a blank form if the user is not logged in

    # If the Stripe public key is missing, display a warning message
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    # Set the context for rendering the checkout page
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,  # Send the client secret for Stripe on the frontend
    }

    return render(request, template, context)  # Render the checkout page with the context


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    This view is triggered after a successful payment, and it displays a success message and order details.
    """
    save_info = request.session.get('save_info')  # Check if the user opted to save their info
    order = get_object_or_404(Order, order_number=order_number)  # Get the order using the order number

    # Fetch the user's profile and link it to the order
    profile = UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    if save_info:  # If the user opted to save their info, update their profile with the order details
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()  # Save the updated profile info

    # Show a success message to the user with the order number and email confirmation
    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    # Clear the basket from the session after the order is complete
    if 'basket' in request.session:
        del request.session['basket']

    # Set the context for the checkout success page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,  # Pass the order object to the success template
    }

    return render(request, template, context)  # Render the success page with the order details