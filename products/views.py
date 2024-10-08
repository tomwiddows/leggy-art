from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from .models import Print, Category

# Create your views here.

def all_prints(request):
    """ A view to show individual product details """

    products = Print.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                
                get_params = request.GET.copy()
                get_params.pop('q', None)
                
                # Construct new URL without 'q' parameter
                path = request.path
                if get_params:
                    path += '?' + urlencode(get_params)
                
                return HttpResponseRedirect(path)
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/prints.html', context)


def print_detail(request, print_id):
    """ A view to show all prints, including sorting and search queries """

    product = get_object_or_404(Print, pk=print_id)

    context = {
        'product': product,
    }

    return render(request, 'products/print_detail.html', context)