from django.shortcuts import render
from blog.models import Blog
from .models import *
# Create your views here.


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'blogs': blogs,
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about-us.html')

def our_team(request):
    return render(request, 'team.html')

def base_admin(request):
    return render(request, 'admin_panel/index.html')


