from rest_framework import serializers
from api.products.models import Product
from .models import CartItem


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(default=1)

class RemoveFromCartSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

