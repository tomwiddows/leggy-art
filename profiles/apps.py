# Install AppConfig from django, to identify which configuration to use
from django.apps import AppConfig


# Define profiles configuration
class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
