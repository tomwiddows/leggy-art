from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    # prevents users from manually accessing the URL by typing /checkout
    if not basket:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q8QkgRodHjT6qLrgDDvYs21aiyZhsrqbR5AWoetCcCuOJbfAg3fJztGtFC8Bw3Vrv4vqwiS0uJZX7t4noBtUHU800z2B0nDNp',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)