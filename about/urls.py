from django.urls import path
from blog.views import blogsingl, blog, blogform
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about'),
    path('our-team/', our_team, name='our-team'),
    path('admin_panel', base_admin, name='base_admin'),
    path('blogsingl/<str:slug>', blogsingl, name='blogsingl'),
    path('blog/', blog, name='blog'),
    path('adminblog/', blogform, name='blogform')
]

