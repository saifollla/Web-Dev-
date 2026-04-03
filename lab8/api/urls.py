from django.urls import path,include 
from .views import CategoryViewSet, ProductViewSet, product_list, product_detail, category_list, category_detail, category_products
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = [
    
    path('', include(router.urls)),
]
