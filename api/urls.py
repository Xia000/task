from django.urls import path
from . import views


urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('product/', views.productList, name='product_list'),
    path('product-detail/<str:pk>/', views.productDetail, name='product_detail'),
    path('create-product/', views.addProduct, name='create_product'),
    path('product-update/<str:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<str:pk>/', views.deleteProduct, name='delete_product'),


    path('category/', views.categoryList, name='category_list'),
    path('create-category/', views.addCategory, name='create_category'),

]


