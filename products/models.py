from django.db import models
from django.contrib.auth.models import User

class ProductManager(models.Manager):
    def get_available_products(self):
        return Product.objects.filter(stock__gt=0)

class CartManager(models.Manager):
    def get_cart_total(self):
        return 100

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.category_name


class ProductTag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self): return f'{self.name} - {self.id}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(ProductTag, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    objects = ProductManager()

    def __str__(self): return f'{self.name}-{self.id}'


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    objects = CartManager()

    class Meta:
        unique_together = ['user', 'product']

    @property
    def total_price(self):
        return self.quantity*self.product.price
