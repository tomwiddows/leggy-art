from django.urls import path # Import the path function for routing URLs
from . import views # Import views from basket app

# Define url paths for all links within home app
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
]