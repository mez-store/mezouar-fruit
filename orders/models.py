from django.db import models
from products.models import Product


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    email = models.EmailField(blank=True, null=True)

    delivery_type = models.CharField(
        max_length=20,
        choices=[
            ("pickup", "استلام من المحل"),
            ("home", "توصيل إلى المنزل"),
        ]
    )

    address = models.TextField(
        max_length=255,
        blank=True,
        null=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"طلب #{self.id} - {self.name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"