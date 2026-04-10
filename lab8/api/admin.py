from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'count', 'is_active', 'category')

    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description', 'price', 'category__name')
    list_editable = ('price', 'count', 'is_active', 'name')

