from rest_framework import viewsets
from .serializers import ProductSerializers  # Adjust the import path
from .models import Product  # Import the Product model

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializers
