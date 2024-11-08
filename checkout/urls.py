# Import the path function for routing URLs
from django.urls import path
# Import views from the basket app to handle requests
from . import views
# Import webhook handling for payment processing
from .webhooks import webhook


# Define URL paths for all links within the checkout app
urlpatterns = [
    # Path for the checkout page where users can review and confirm orders
    path('', views.checkout, name='checkout'),
    
    # Path for the checkout success page after a successful order placement
    path('checkout_success/<order_number>', views.checkout_success, 
         name='checkout_success'),
    
    # Path to cache checkout data, usually used for saving basket state
    path('cache_checkout_data/', views.cache_checkout_data, 
         name='cache_checkout_data'),
    
    # Path for webhook URL to handle incoming payment notifications
    path('wh/', webhook, name='webhook'),
]
