# Import the path function for routing URLs
from django.urls import path
# Import views from basket app
from . import views

# Define url paths for all links within profiles app
urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>', 
        views.order_history, 
        name='order_history'
    ),
]
