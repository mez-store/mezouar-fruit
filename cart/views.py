from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from products.models import Product
from .cart import Cart


# ✅ إضافة منتج للسلة
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    # ✅ كمية افتراضية = 1
    quantity = request.POST.get("quantity", 1)

    # ✅ محاولة الإضافة
    success = cart.add(product=product, quantity=quantity)

    if success:
        messages.success(request, "✅ تمت إضافة المنتج إلى السلة")
    else:
        messages.error(request, "❌ هذا المنتج غير متوفر حاليا")

    return redirect("cart_detail")


# ✅ عرض السلة
def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})


# ✅ حذف منتج من السلة
def cart_remove(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    messages.warning(request, "🗑 تم حذف المنتج من السلة")

    return redirect("cart_detail")