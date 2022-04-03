from django.urls import path

from .views import *


urlpatterns = [
    path('', user_login, name='login'),
    path('add-product/', add_product, name='add_product'),
    path('product/', admin_product, name='admin_product'),
    path('brand-edit/<slug:slug>/', editbrand, name='editbrand'),
    path('product-edit/<slug:slug>/', editproduct, name='editproduct'),
    path('delete/<int:pk>/', delete_product, name='delete'),
    path('add-admin/', addAdmin, name='add-admin'),
    path('logout/', user_logout, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('vacancy/', admin_vacancy, name='admin-vacancy'),
    path('delete-vacancy/<int:id>/', delete_vacancy, name='delete-vacancy'),
    path('delete-resume/<int:id>/', delete_resume, name='delete-resume'),
    path('download-resume/<int:id>/', download_resume, name='download-resume'),
    path('<str:username>/', adminPanel, name='admin-panel'),
]
