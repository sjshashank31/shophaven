from django.contrib import admin
from .models import Product, ProductCategory, CartItem


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price']
    autocomplete_fields = ("categories",) # For Select Drop Down UI


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',) # We are using autocomplete field in ProductAdmin


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(CartItem, CartItemAdmin)