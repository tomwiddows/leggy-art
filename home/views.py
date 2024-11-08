# Import render from django for loading pages
from django.shortcuts import render


# Index view for rendering index.html template
def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


# About view for rendering about.html template
def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')
