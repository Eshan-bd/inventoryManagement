from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.add_product, name='add_product'),

    path('categories/add/', views.add_category, name='add_category'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>', views.product_list_by_category, name='product_list_by_category'),
]