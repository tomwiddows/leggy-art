from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_prints, name='products'),
    path('<print_id>', views.print_detail, name='product_detail'),
]