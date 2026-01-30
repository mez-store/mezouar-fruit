from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'sell_unit',
        'price',
        'step',
        'available'
    )
    list_filter = ('sell_unit', 'available', 'category')
    search_fields = ('name',)