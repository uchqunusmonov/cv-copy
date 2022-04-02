from unicodedata import name
from django.urls import path

from .views import *


urlpatterns = [
    path('', user_login, name='login'),
    path('add-admin/', addAdmin, name='add-admin'),
    path('logout/', user_logout, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('vacancy/', admin_vacancy, name='admin-vacancy'),
    path('delete/<int:id>/', delete_vacancy, name='delete-vacancy'),
    path('<str:username>/', adminPanel, name='admin-panel'),
]
