# Install AppConfig from django, to identify which configuration to use
from django.apps import AppConfig
# Import messages from django
from django.contrib import messages


# Define checkout configuration
class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # Attempt to initialise the checkout app
    try:
        def ready(self):
            import checkout.signals
    except Exception as e:
        messages.error(error, 'e')
