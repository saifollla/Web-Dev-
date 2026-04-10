from django.urls import path,include 
#from api.views import fbv
from rest_framework.routers import DefaultRouter
from api import views

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)
# urlpatterns = [
    
#     path('', include(router.urls)),
# ]


urlpatterns = [
#     path('products/', fbv.products_list),
#     path('products/<int:product_id>/', fbv.product_detail),

    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),

    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),
]

