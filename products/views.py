from django.shortcuts import render
from .models import Print

# Create your views here.

def all_prints(request):
    """ A view to show all prints, including sorting and search queries """#

    prints = Print.objects.all()

    contex = {
        'products': prints,
    }

    return render(prints, 'products/prints.html', context)
