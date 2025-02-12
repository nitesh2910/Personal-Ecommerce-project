from django.urls import path
from .views import ProductListCreateAPIView,CategorListAPIView,UserListCreateAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('categories/', CategorListAPIView.as_view(), name='category-list'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
]
