from django.shortcuts import render, HttpResponse , redirect
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from .decorators import unauthorized_user
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


# Create your views here.



def index(request):
    return render(request, 'base.html')




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('api_overview')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('api_overview')
    else:
        return HttpResponse("404 - Not found")


def signup(request):
    
    if request.method == 'POST':

        username = request.POST['fullName']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        

        if len(username) < 3:
            messages.error( request, "Username must be greater than 3 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error( request, "Username must be alphanumeric")
            return redirect('home')
        
        if User.objects.filter(username=username).exists():
            messages.error( request, "Username already exists")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error( request, "Email already exists")
            return redirect('home')


        if password1 != password2:
            messages.error( request, "Password did not match")
            return redirect('home')
        
        user = User.objects.create_user(username, email,password1)
        user.save()
  
        
        messages.success(request, " Your Account has been successfully created")
        return redirect('api_overview')

    else:
        return HttpResponse("404 - Not found")


def logoutHandle(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect("home")



@api_view(['GET'])
def apiOverview(request):

    permission_classes = (IsAuthenticated,)

    api_urls = {
        'Categories': '/category/',
        'Create Category': '/create-category/',
        'Update Category': '/category-update/<str:pk>/',
        'Delete Category': '/category-delete/<str:pk>/',

        'Products': '/product/',
        'Create': '/create-product/',
        'Update': '/update-product/<str:id>/',
        'Delete': '/product-delete/<str:id>/',
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


