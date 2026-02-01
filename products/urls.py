from django.urls import path
from . import views
from .views import create_admin

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("create-admin/", create_admin),
]