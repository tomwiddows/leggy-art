from django.shortcuts import render, get_object_or_404
from .models import Print

# Create your views here.

def all_prints(request):
    """ A view to show individual product details """

    products = Print.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/prints.html', context)


def print_detail(request, print_id):
    """ A view to show all prints, including sorting and search queries """

    product = get_object_or_404(Print, pk=print_id)

    context = {
        'product': product,
    }

    return render(request, 'products/print_detail.html', context)