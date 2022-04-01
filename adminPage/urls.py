from unicodedata import name
from django.urls import path

from .views import *


urlpatterns = [
    path('', adminPanel, name='admin-panel'),
    path('login/', user_login, name='login'),
]
