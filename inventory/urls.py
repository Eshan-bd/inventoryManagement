from django.urls import path
from . import views
from .views import add_category, category_list

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.add_product, name='product_new'),

    path('categories/add/', add_category, name='add_category'),
    path('categories/', category_list, name='category_list'),
]