"""
ASGI config for leggy_art project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os  # Import os module to interact with the operating system
from django.core.asgi import get_asgi_application  # Import the ASGI application handler from Django

# Sets the default settings module for the Django project, which points to 'leggy_art.settings'.
# This is required to configure the Django application for ASGI.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leggy_art.settings')

# Gets the ASGI application callable from Django's core that will handle ASGI requests.
# This is used to run the ASGI server and manage incoming connections.
application = get_asgi_application()