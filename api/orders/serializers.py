from rest_framework import serializers
from .models import OrderItem, Order

def OrderItemSerializer(serializers.ModelSerializers):
	class Meta:
		model = OrderItem
		fields = '__all__'


def OrderSerializer(serializers.ModelSerializers):
	items = OrderItemSerializer(many = True)


	model = OrderItem
	fields = '__all__'

