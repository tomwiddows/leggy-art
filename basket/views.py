# Importing required modules and classes from Django
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
# Import the Print model from the products app
from products.models import Print


def view_basket(request):
    """ A view to render the basket contents page """
    # Render the basket's HTML template, which displays the contents of the
    #  user's basket.
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    # Fetch the product based on the item_id passed in the URL.
    # If the product doesn't exist, return a 404 error.
    product = get_object_or_404(Print, pk=item_id)

    # Retrieve the quantity the user wants to add from the POST data, ensuring
    # it is an integer.
    quantity = int(request.POST.get('quantity'))

    # Get the URL to redirect to after adding the item (this is helpful for
    # redirecting back to the product page).
    redirect_url = request.POST.get('redirect_url')

    # Retrieve the current basket from the session, or initialize it as an 
    # empty dictionary if it doesn't exist.
    basket = request.session.get('basket', {})

    # If the item already exists in the basket, update the quantity.
    if item_id in basket:
        # Add the requested quantity to the current quantity.
        basket[item_id] += quantity
        # Show success message.
        message = f'Updated {product.name} quantity to {basket[item_id]}'
        messages.success(request, message)

    else:
        # If the item is not in the basket, add it with the specified quantity
        basket[item_id] = quantity
        # Show success message.
        messages.success(request, f'Added {product.name} to your basket')

    # Save the updated basket back to the session.
    request.session['basket'] = basket

    # Redirect the user to the URL specified in the form (typically the
    # product detail page).
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product in the shopping bag """
    # Get the product based on the item_id.
    product = get_object_or_404(Print, pk=item_id)

    # Retrieve the new quantity from the POST data.
    quantity = int(request.POST.get('quantity'))

    # Retrieve the current basket from the session.
    basket = request.session.get('basket', {})

    # If the quantity is greater than zero, update the basket with the new
    # quantity.
    if quantity > 0:
        basket[item_id] = quantity
        message = f'Updated {product.name} quantity to {basket[item_id]}'
        messages.success(request, message)
    else:
        # If the quantity is zero or negative, remove the item from the basket
        basket.pop(item_id)  # `pop()` removes the item with the given key
                             # (item_id) from the basket.
        messages.success(request, f'Removed {product.name} from your basket')

    # Save the updated basket back to the session.
    request.session['basket'] = basket

    # Redirect the user back to the basket page to see the updated contents.
    return redirect(reverse('view_basket'))  # Using `reverse()` to get the
                                             # URL of the `view_basket` view.


def remove_from_basket(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        # Get the product to remove based on the item_id.
        product = get_object_or_404(Print, pk=item_id)

        # Retrieve the current basket from the session.
        basket = request.session.get('basket', {})

        # Remove the item from the basket using `pop()`, which also removes
        # the item from the dictionary.
        basket.pop(item_id)

        # Show a success message to the user.
        messages.success(request, f'Removed {product.name} from your basket')

        # Save the updated basket back to the session.
        request.session['basket'] = basket

        # Return a 200 HTTP response, indicating the operation was successful.
        return HttpResponse(status=200)

    except Exception as e:
        # If there is an error (e.g., the item doesn't exist or another issue
        # occurs), show an error message.
        messages.error(request, f'Error removing item: {e}')

        # Return a 500 HTTP response, indicating there was an error processing
        # the request.
        return HttpResponse(status=500)
