from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),

    path('categories/add/', views.add_category, name='add_category'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.product_list_by_category, name='product_list_by_category'),
]