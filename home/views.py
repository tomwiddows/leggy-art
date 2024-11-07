from django.shortcuts import render # Import render from django for loading pages


# Index view for rendering index.html template
def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

# About view for rendering about.html template
def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')