# Install AppConfig from django, to identify which configuration to use
from django.apps import AppConfig


# Define home configuration
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
