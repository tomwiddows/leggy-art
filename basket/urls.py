from django.urls import path  # Import the path function for routing URLs
from . import views  # Import views from basket app

# Define url paths for all links within basket app
urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<item_id>/', views.adjust_basket, name='adjust_basket'),
    path('remove/<item_id>/', views.remove_from_basket, 
            name='remove_from_basket'
        ),
]
