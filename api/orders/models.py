from django.db import models
from django.conf import settings
from api.products.models import Product
from api.users.models import CustomUser

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem', related_name='orders')  # Use related_name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.pk}"

    def get_total(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_item_price()
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # Use related_name

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price
