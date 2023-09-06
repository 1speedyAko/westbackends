from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('name','description','price','stock')
		fields = '__all__'