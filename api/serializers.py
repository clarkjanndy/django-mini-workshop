from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

from api.models import Product

class ProductSerializer(serializers.ModelSerializer): 
    created_by = serializers.PrimaryKeyRelatedField(read_only= True)
    created_by_details = serializers.SerializerMethodField()
       
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_created_by_details(self, instance):
        return instance.created_by.get_full_name()
        