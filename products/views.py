from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, redirect
from .forms import ProductForm
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

def create_admin(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "products/create.html", {"form": form})