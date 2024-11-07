from django.urls import path # Import the path function for routing URLs
from . import views # Import views from basket app
from .webhooks import webhook # Import webhooks for webhook handling for payments

# Define url paths for all links within checkout app
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]