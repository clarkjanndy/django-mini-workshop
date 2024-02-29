from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import ProductSerializer
from api.models import Product

# Create your views here.
class ProductListCreate(ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        querset =  Product.objects.all()
        serializer = ProductSerializer(querset, many=True)
        
        return Response({
            "type": "success",
            "data": serializer.data
        })
        
    def post(self, request, *args, **kwargs):
       data = request.data
       serializer = ProductSerializer(data=data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       
       return Response({
            "type": "success",
            "data": serializer.data
        })
       
class ProductById(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ProductSerializer(obj)
        
        return Response({
            "type": "success",
            "data": serializer.data
        })
        
    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        data = request.data
        serializer = ProductSerializer(obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response({
            "type": "success",
            "data": serializer.data
        })
        
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        data = response.data
        
        return Response({
            "type": "success",
            "data": {
                "message": 'Product deleted succesfully.'
            }
        })
        