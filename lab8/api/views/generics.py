from rest_framework import generics
from api.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer
class ProductListAPIView(generics.ListCreateAPIView): #get post
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView): #get put delete
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id' 



class CategoryListAPIView(generics.ListCreateAPIView): #category list and create
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView): #get put delete
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = 'category_id' 