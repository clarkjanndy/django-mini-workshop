from django.urls import path
from api import views


urlpatterns = [
    path('products', views.ProductListCreate.as_view()),  
    path('products/<int:pk>', views.ProductById.as_view()),   
]
