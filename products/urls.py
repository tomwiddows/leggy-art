# Import the path function for routing URLs
from django.urls import path
# Import views from basket app
from . import views

# Define url paths for all links within products app
urlpatterns = [
    path('', views.all_prints, name='products'),
    path('<int:print_id>/', views.print_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:print_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:print_id>/', views.delete_product, name='delete_product')
]
