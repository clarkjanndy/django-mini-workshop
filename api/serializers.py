from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Product

class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'