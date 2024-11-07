# Import necessary modules
from decimal import Decimal  # Used for precise decimal arithmetic
from django.conf import settings  # To access the settings like delivery thresholds and fees
from django.shortcuts import get_object_or_404  # Used to retrieve a product or raise a 404 error if not found
from products.models import Print  # The Print model, representing products in the store

def basket_contents(request):
    """
    Retrieves the contents of the shopping basket from the session,
    calculates totals, and returns the data for rendering in the template.
    """

    # Initialize variables
    basket_items = []  # Will hold the list of items in the basket with details (e.g., product, quantity, subtotal)
    total = 0  # Holds the total value of the basket (before delivery costs)
    basket = request.session.get('basket', {})  # Retrieve the basket from session (default to empty if not found)

    # Loop through the basket to calculate subtotals and total cost
    for item_id, quantity in basket.items():
        if quantity is not None:  # Ensure there's a valid quantity (not None)
            product = get_object_or_404(Print, pk=item_id)  # Get the product using its ID (raise 404 if not found)
            subtotal = quantity * product.price  # Calculate the subtotal for this product
            total += subtotal  # Add the subtotal to the total value of the basket

            # Append product details to the basket_items list
            basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'subtotal': subtotal,
                'product': product,  # Add the product object to the context for use in templates
            })

    # Count the number of unique items in the basket
    product_count = len(basket_items)

    # Calculate delivery cost and check for free delivery threshold
    if total < settings.FREE_DELIVERY_THRESHOLD and total != 0:
        # If the total is less than the free delivery threshold, calculate delivery fee
        delivery = Decimal(settings.BASELINE_DELIVERY_FEE + (total * settings.EXTRA_DELIVERY_PERCENTAGE) / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total  # How much more the user needs to spend for free delivery
    else:
        # If the total is above the free delivery threshold, no delivery fee
        delivery = 0
        free_delivery_delta = 0

    # Calculate the grand total (total + delivery fee)
    grand_total = delivery + total

    # Prepare the context to be passed to the template
    context = {
        'basket_items': basket_items,  # List of items with details for display
        'product_count': product_count,  # The number of unique products in the basket
        'total': total,  # The total value of the items in the basket (before delivery)
        'delivery': delivery,  # Delivery fee (if applicable)
        'free_delivery_delta': free_delivery_delta,  # How much more the user needs to spend for free delivery
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,  # The value threshold for free delivery
        'grand_total': grand_total,  # Final total (including delivery fee)
    }

    # Return the context so it can be used in the view
    return context