from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from api.products.models import Product
from django.shortcuts import get_object_or_404


class CartView(viewsets.ViewSet):
    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        # Serialize the cart items and return the data
        serializer = CartItemSerializer(cart_items, many = True)
        # Implement your serializer logic


        return Response(serializer.data)

class AddToCartView(viewsets.ViewSet):
    def post(self, request):
        serializer = AddToCartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data.get('quantity', 1)

            product = get_object_or_404(Product, id=product_id)
            cart, created = Cart.objects.get_or_create(user=request.user)

            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item.quantity = quantity
                cart_item.save()

            return Response({'message': 'Item added to cart successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCartView(viewsets.ViewSet):
    def post(self, request):
        serializer = RemoveFromCartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            cart = Cart.objects.get_or_create(user=request.user)
            cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()

            if cart_item:
                cart_item.delete()
                return Response({'message': 'Item removed from cart successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Item not found in the cart'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

