from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products
    })

import os
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    username = os.environ.get("ADMIN_USER")
    password = os.environ.get("ADMIN_PASS")
    email = os.environ.get("ADMIN_EMAIL")

    if not username or not password or not email:
        return HttpResponse("Missing admin environment variables")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        return HttpResponse("Admin created")

    return HttpResponse("Admin already exists")
