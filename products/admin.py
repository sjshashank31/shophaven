from django.contrib import admin
from .models import Product, ProductTag, CartItem, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price']
    autocomplete_fields = ("tags",) # For Select Drop Down UI


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name',) # We are using autocomplete field in ProductAdmin


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'parent_category']
    autocomplete_fields = ('parent_category', )
    search_fields = ('category_name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, ProductTagAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Category, CategoryAdmin)