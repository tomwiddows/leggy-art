# Import the path function for routing URLs
from django.urls import path
# Import views from basket app
from . import views

# Define url paths for all links within home app
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
]
