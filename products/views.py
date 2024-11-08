# Import necessary modules and functions from Django
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode

# Import models and forms for the products
from .models import Print, Category
from .forms import ProductForm


def all_prints(request):
    """
    A view to show all prints/products with search, filter, and sorting functionality
    """

    # Start with all products
    products = Print.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Handle GET parameters for search, filter, and sorting
    if request.GET:
        # Sort products based on the 'sort' query parameter
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # If sorting by name, apply a case-insensitive sort
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            # If sorting by category, sort by the category's name
            if sortkey == 'category':
                sortkey = 'category__name'
            # Handle sorting direction (ascending or descending)
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  # Apply descending order
            # Order the products based on the selected sort key
            products = products.order_by(sortkey)

        # Filter products by selected categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # Multiple categories can be selected
            products = products.filter(category__name__in=categories)  # Filter products by categories
            categories = Category.objects.filter(name__in=categories)  # Get category objects for display

        # Filter products by a search query
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # If no query is entered, remove the 'q' parameter and redirect
                get_params = request.GET.copy()
                get_params.pop('q', None)
                # Rebuild the URL without the 'q' parameter
                path = request.path
                if get_params:
                    path += '?' + urlencode(get_params)
                return HttpResponseRedirect(path)

            # Perform a case-insensitive search in both name and description fields
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Create a string that describes the current sorting (for display purposes)
    current_sorting = f'{sort}_{direction}'

    # Pass the products, query, and other context variables to the template
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    # Render the products page with the context data
    return render(request, 'products/prints.html', context)


def print_detail(request, print_id):
    """
    A view to show the details of a single print/product
    """

    # Get the product by its ID, or return a 404 error if it doesn't exist
    product = get_object_or_404(Print, pk=print_id)

    # Pass the product object to the template for rendering
    context = {
        'product': product,
    }

    # Render the product detail page
    return render(request, 'products/print_detail.html', context)


@login_required
def add_product(request):
    """
    Add a new product to the store (only accessible to store owners)
    """
    
    # Check if the user is a store owner (superuser)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Handle POST request to create a new product
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data as a new product in the database
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('print_detail', args=[product.id]))  # Redirect to the product detail page
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()  # Render a blank form if it's a GET request

    # Pass the form to the template
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    # Render the add product page with the form
    return render(request, template, context)


@login_required
def edit_product(request, print_id):
    """
    Edit an existing product in the store (only accessible to store owners)
    """
    
    # Check if the user is a store owner (superuser)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get the product to be edited by its ID
    product = get_object_or_404(Print, pk=print_id)

    # Handle POST request to update the product
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Save the updated product data
            product = form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('print_detail', args=[product.id]))  # Redirect to the product detail page
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)  # Populate the form with the existing product data
        messages.info(request, f'You are editing {product.name}')  # Inform the user which product they are editing

    # Pass the form and product data to the template
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
        'image_1_path': product.image_1.url,  # Provide the URL for the first product image
        'image_2_path': product.image_2.url,  # Provide the URL for the second product image
    }

    # Render the edit product page with the form and product data
    return render(request, template, context)


@login_required
def delete_product(request, print_id):
    """
    Delete a product from the store (only accessible to store owners)
    """
    
    # Check if the user is a store owner (superuser)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get the product to be deleted by its ID
    product = get_object_or_404(Print, pk=print_id)
    
    # Delete the product from the database
    product.delete()
    messages.success(request, 'Product deleted!')

    # Redirect to the products page (listing all available products)
    return redirect(reverse('products'))
