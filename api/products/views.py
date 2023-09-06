from django.shortcuts import render
from rest_framework import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('name')
	serializer_class = ProductSerializer
# Create your views here.
