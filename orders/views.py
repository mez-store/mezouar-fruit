from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Order
from cart.cart import Cart
import urllib.parse


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        delivery_type = request.POST.get('delivery_type')
        address = request.POST.get('address', '')

        # 🔢 حساب المجموع
        total_price = 0
        products_text = ""

        for item in cart:
            product = item['product']
            quantity = item['quantity']
            price = item['price']
            total = price * quantity

            total_price += total

            products_text += (
                f"• {product.name} — {quantity} × {price} دج = {total} دج\n"
            )

        # 💾 حفظ الطلب
        order = Order.objects.create(
            name=name,
            phone=phone,
            email=email,
            delivery_type=delivery_type,
            address=address,
            total_price=total_price
        )

        # 📧 رسالة الإيميل
        email_message = f"""
طلب جديد من متجر الإخوة مزوار

الاسم: {name}
الهاتف: {phone}

المنتجات:
{products_text}

المجموع: {total_price} دج
"""

        send_mail(
            '🛒 طلب جديد من المتجر',
            email_message,
            settings.EMAIL_HOST_USER,
            ['mezouarabderrahmane04@gmail.com'],
            fail_silently=False,
        )

        # 📱 رسالة واتساب
        whatsapp_message = f"""
🛒 طلب جديد

الاسم: {name}
الهاتف: {phone}

المنتجات:
{products_text}

💰 المجموع: {total_price} دج
"""

        encoded = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/213673619216?text={encoded}"

        # 🧹 تفريغ السلة
        cart.clear()

        # ✅ التحويل لصفحة النجاح
        return redirect('order_success')

    return render(request, 'orders/create.html')

def order_success(request):
    return render(request, 'orders/success.html')