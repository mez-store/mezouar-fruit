from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    SELL_UNIT_CHOICES = [
        ('kg', 'بالكيلوغرام'),
        ('piece', 'بالقطعة'),
    ]

    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    sell_unit = models.CharField(
        max_length=10,
        choices=SELL_UNIT_CHOICES,
        default='kg'
    )

    price = models.FloatField(
        help_text="السعر للوحدة (كغ أو قطعة)"
    )

    step = models.FloatField(
        default=0.5,
        help_text="مثلا 0.5 كغ أو 1 قطعة"
    )

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
