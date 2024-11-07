"""
WSGI config for leggy_art project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os  # Import os module to interact with the operating system
from django.core.wsgi import get_wsgi_application  # Import the WSGI application handler from Django

# Sets the default settings module for the Django project, which points to 'leggy_art.settings'.
# This is required to configure the Django application for WSGI.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'leggy_art.settings')

# Gets the WSGI application callable from Django's core that will handle WSGI requests.
# This is used to run the WSGI server and manage incoming connections.
application = get_wsgi_application()