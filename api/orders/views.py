from django.shortcuts import render
from rest_framework import generics
from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpadteDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderItemCreateView(generics.ItemCreateAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemSerializer