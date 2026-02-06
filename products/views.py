from django.shortcuts import render
from .models import Product, Category

import os
from django.contrib.auth.models import User
from django.http import HttpResponse


# ==============================
# ✅ الصفحة الرئيسية + البحث
# ==============================
def product_list(request):

    # جميع الأصناف
    categories = Category.objects.all()

    # المنتجات المتوفرة فقط
    products = Product.objects.filter(available=True)

    # ✅ Search
    query = request.GET.get("q")
    if query:
        products = products.filter(name__icontains=query)

    return render(request, "products/product_list.html", {
        "categories": categories,
        "products": products,
        "query": query,
    })


# ==============================
# ✅ إنشاء Admin تلقائيا (Render)
# ==============================
def create_admin(request):

    username = os.environ.get("ADMIN_USER")
    password = os.environ.get("ADMIN_PASS")
    email = os.environ.get("ADMIN_EMAIL")

    if not username or not password or not email:
        return HttpResponse("❌ Missing admin environment variables")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        return HttpResponse("✅ Admin created successfully")

    return HttpResponse("ℹ️ Admin already exists")