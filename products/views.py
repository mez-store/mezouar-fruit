from django.shortcuts import render
from .models import Product, Category

# ==============================
# ✅ الصفحة الرئيسية + البحث
# ==============================
def product_list(request):

    # جميع الأصناف
    categories = Category.objects.all()

    # ✅ عرض جميع المنتجات (متوفر + غير متوفر)
    products = Product.objects.all()

    # ✅ Search
    query = request.GET.get("q")
    if query:
        products = products.filter(name__icontains=query)

    return render(request, "products/product_list.html", {
        "categories": categories,
        "products": products,
        "query": query,
    })