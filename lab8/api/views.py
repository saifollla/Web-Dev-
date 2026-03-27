from django.http import JsonResponse
from .models import Product, Category
# Create your views here.

def product_list(request):
    products = Product.objects.all()
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