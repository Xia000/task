from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
   
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),



    path('home', views.index, name='home'),
    path('', views.apiOverview, name='api_overview'),

    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logoutHandle, name="handleLogout"),


    path('product/', views.productList, name='product_list'),
    path('product-detail/<str:pk>/', views.productDetail, name='product_detail'),
    path('create-product/', views.addProduct, name='create_product'),
    path('product-update/<str:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<str:pk>/', views.deleteProduct, name='delete_product'),


    path('category/', views.categoryList, name='category_list'),
    path('create-category/', views.addCategory, name='create_category'),



]


