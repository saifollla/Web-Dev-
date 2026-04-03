from django.http import JsonResponse
from .models import Product, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    category_id = request.GET.get('category')
    active = request.GET.get('active')
    search = request.GET.get('search')
    if category_id:
        products = products.filter(category_id=category_id)
    if active is not None:
        is_active = active.lower() == 'true'
        products = products.filter(is_active=is_active)
    if search:
        products = products.filter(name__icontains=search)
    data = {'products': list(products.values())}
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category_id': product.category.id
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    
def category_list(request):
    categories = Category.objects.all()
    return JsonResponse(list(categories.values('id', 'name')), safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse({'id': category.id, 'name': category.name})
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
        products = category.products.all() 
        return JsonResponse(list(products.values()), safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    
class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = category.products.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer