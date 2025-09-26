from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.price() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def price(self):
        return self.product.price * self.quantity

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='Product')
#     quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
#     session_key = models.CharField(max_length=40, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

#     class Meta:
#         db_table = 'order'
#         verbose_name = 'Order'
#         verbose_name_plural = 'Order'

#     def product_total(self):
#         return self.product.price * self.quantity
