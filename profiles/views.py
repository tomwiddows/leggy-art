# Import necessary modules and functions from Django
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Import models and forms for user profiles
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile and allow updating their details. """
    
    # Retrieve the UserProfile object for the current user (or 404 if not found)
    profile = get_object_or_404(UserProfile, user=request.user)

    # Handle the form submission (when method is POST)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        
        # Check if the form is valid and save the data if it is
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update complete')  # Success message
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')  # Error message
    else:
        # Pre-populate the form with the current user profile data if it's a GET request
        form = UserProfileForm(instance=profile)

    # Retrieve the user's past orders
    if not request.user.is_superuser:
        orders = profile.orders.all()
    else:
        orders = Order.objects.all()


    # Define the context for the template
    template = 'profiles/profile.html'
    context = {
        'form': form,  # The profile form (for updating user details)
        'orders': orders,  # The user's order history, or if superuser, all orders from the site
        'on_profile_page': True,  # Flag to indicate the current page is the profile page
    }

    # Render the profile template with the context data
    return render(request, template, context)


def order_history(request, order_number):
    """ Display the details of a specific past order, accessed from the profile. """
    
    # Retrieve the Order object based on the order number (or 404 if not found)
    order = get_object_or_404(Order, order_number=order_number)

    # Provide an info message that explains this is a past confirmation for the order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # Define the context for the order history template
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,  # The specific order details
        'from_profile': True,  # Flag to indicate this view was accessed from the profile page
    }

    # Render the order history template with the order details
    return render(request, template, context)
