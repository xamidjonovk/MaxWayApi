from django.urls import path
from .views import *
urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='categories-list'),

    path('products/', ProductView.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductView.as_view(), name='products-list'),

    path('orders/', OrderView.as_view(), name='orders-list'),
    path('orders/<int:pk>/', OrderView.as_view(), name='orders-list'),

    path('customers/', CustomerView.as_view(), name='cusromers-list'),
    path('customers/<int:pk>/', CustomerView.as_view(), name='cusromers-list'),

    path('orderproduct/', OrderProductView.as_view(), name='orderproduct-list'),
    path('orderproduct/<int:pk>/', OrderProductView.as_view(), name='orderproduct-list'),
]