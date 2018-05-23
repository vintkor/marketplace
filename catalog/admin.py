from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductVariant,
    ProductImage,
)


class ProductImageInline(admin.TabularInline):
    extra = 0
    model = ProductImage


class ProductVariantInline(admin.TabularInline):
    extra = 0
    model = ProductVariant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductVariantInline,)
    list_display = (
        'title',
        'vendor',
    )


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline,)
    list_display = (
        '__str__',
        'get_currency',
        'get_course',
        'get_price',
        'is_main',
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
