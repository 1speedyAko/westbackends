from django.shortcuts import render
from rest_framework import generics
from .models import OrderItem, Order
from .serializers import OrderItemSerializer, OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class OrderItemCreateView(generics.CreateAPIView):
	queryset = OrderItem.objects.all()
	serializer_class = OrderItemSerializer