from django.db import models
from products.models import Product

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(
        blank=True,
        null=True
    )
    delivery_type = models.CharField(max_length=20)
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
        return self.name


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
    price = models.IntegerField()
    quantity = models.FloatField()

    def __str__(self):
        return str(self.id)