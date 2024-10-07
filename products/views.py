from django.shortcuts import render
from .models import Print

# Create your views here.

def all_prints(request):
    """ A view to show all prints, including sorting and search queries """

    products = Print.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/prints.html', context)
