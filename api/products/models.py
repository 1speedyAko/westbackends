# products/models.py
from api.category.models import Category
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default = True , blank = True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True , null = True)
    image = models.ImageField(upload_to='products/', blank = True , null = True)  # This field is for product images
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
