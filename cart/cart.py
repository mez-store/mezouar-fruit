from decimal import Decimal
from products.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    # ✅ إضافة منتج
    def add(self, product, quantity=1):

        product_id = str(product.id)

        # ❌ ممنوع إضافة منتج غير متوفر
        if not product.available:
            return False

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price),
                "name": product.name,
            }

        # ✅ الكمية لازم int
        self.cart[product_id]["quantity"] += int(quantity)

        self.save()
        return True

    # ✅ حفظ
    def save(self):
        self.session.modified = True

    # ✅ حذف منتج
    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # ✅ عرض المنتجات
    def __iter__(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    # ✅ مجموع السعر
    def get_total_price(self):
        return sum(item["total_price"] for item in self)

    # ✅ تفريغ السلة
    def clear(self):
        self.session["cart"] = {}
        self.save()