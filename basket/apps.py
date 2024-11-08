# Install AppConfig from django, to identify which configuration to use
from django.apps import AppConfig  

# Define basket configuration
class BasketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
    