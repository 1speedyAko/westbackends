from django.db import models
from api.products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class OrderItem(models.Model):
	product = models.ForeignKey(Product , on_delete = models.CASCADE)
	quantity = models.PositiveIntegerField(default = 1)
	user  =  models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		f"{self.quantity} of {self.product.title}"

	def get_total_item_price(self):
		return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
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