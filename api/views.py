from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category


# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Categories': '/category/',
        'Create Category': '/create-category/',
        'Update Category': '/category-update/<str:pk>/',
        'Delete Category': '/category-delete/<str:pk>/',

        'Products': '/product/',
        'Create': '/create-product/',
        'Update': '/update-product/<int:id>/',
        'Delete': '/delete-product/<int:id>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many= False)
    return Response(serializer.data)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Item successfully deleted")


@api_view(['GET'])
def categoryList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)