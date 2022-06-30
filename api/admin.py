from django.contrib import admin
from .models import Product,Category


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'bus_model', 'category']

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)