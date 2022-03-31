from django.urls import path
from .views import career

urlpatterns = [
    path('', career, name='career'),
]

