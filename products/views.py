from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {
        'categories': categories,
        'products': products
    })

from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products
    })
    
# Create your views here.
