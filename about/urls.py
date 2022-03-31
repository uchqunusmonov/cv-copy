from unicodedata import name
from django.urls import path
from .views import home, about_us
from blog.views import blogsingl, blog
from .views import about_us, base_admin


urlpatterns = [
    path('', home, name='home'),
    path('about', about_us, name='about'),
    path('blogsingl/<str:slug>', blogsingl, name='blogsingl'),
    path('blog/', blog, name='blog'),
    path('admin_panel', base_admin, name='base_admin'),
]

