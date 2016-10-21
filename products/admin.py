from django.contrib import admin
from .models import Product, ProductImage


class ImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    admin.site.register(Product)
    admin.site.register(ProductImage)
