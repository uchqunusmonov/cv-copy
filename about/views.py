from django.shortcuts import render
from blog.models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects.all().order_by('-created_at')[:3]
    context = {
        'blogs': blogs,
    }
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about-us.html')



