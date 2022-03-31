from django.contrib import admin
from django.urls import path
from .views import brand, product_details
urlpatterns = [
    path('product/', brand, name='brand'),
    path('product-details/<slug:slug>/', product_details, name='product_details')
]
