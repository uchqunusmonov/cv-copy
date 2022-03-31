from django.shortcuts import render, redirect
from .models import Blog
from .forms import *
from django.core.paginator import Paginator


# Create your views here.
def blogform(request):
    form = BlogForm(request.POST, request.FILES)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        print(3)
        if form.is_valid():
            print(4)
            form.save()

            return redirect('blogform')
    else:
        form = BlogForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'admin_panel/blog.html', context)

def blog(request):
    form = Blog.objects.all().order_by('-created_at')
    paginating = Paginator(form, 9)
    page = request.GET.get('page')
    form = paginating.get_page(page)


    context = {
        'form': form,
        'paginating': paginating,
    }
    return render(request, 'blog.html', context)


def blogsingl(request, slug):
    forms = Blog.objects.get(slug=slug)
    blogs = Blog.objects.all().order_by('-created_at')[:6]
    context = {
        'forms': forms,
        'blogs': blogs,
    }
    return render(request, 'blogSingl.html', context)
