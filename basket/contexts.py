from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Print

def basket_contents(request):

    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        if quantity is not None:
            product = get_object_or_404(Print, pk=item_id)
            subtotal = quantity * product.price
            total += quantity * product.price
            basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'subtotal': subtotal,
                'product': product,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD and total != 0:
        delivery = Decimal(settings.BASELINE_DELIVERY_FEE + (total * settings.EXTRA_DELIVERY_PERCENTAGE) / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context