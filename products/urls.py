from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.product_list, name='product_list'),
]