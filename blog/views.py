from django.shortcuts import render, redirect
from .models import Blog
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def blog(request):
    form = Blog.objects.all().order_by('-created_at')
    paginating = Paginator(form, 3)
    page = request.GET.get('page')
    form = paginating.get_page(page)

    # forms = BlogForm(request.POST)
    # if request.method == 'POST':
    #     forms = BlogForm(request.POST)
    #     if forms.is_valid():
    #         forms.save()
    #         return redirect('base.html')
    #     else:
    #         forms = BlogForm(request.POST)
    context = {
        'form': form,
        # 'forms':forms,
        'paginating': paginating,
    }
    return render(request, 'blog.html', context)


def blogsingl(request, slug):
    forms = Blog.objects.get(slug=slug)
    blogs = Blog.objects.all().order_by('-created_at')[:6]
    # if 'search' in request.GET:
    #     search = request.GET['search']
    #     blogs = blogs.filter(Q(title__icontains=search) | Q(short_text__icontains=search))
    # else:
    #     blogs = Blog.objects.all().order_by('-created_at')[:4]
    context = {
        'forms': forms,
        'blogs': blogs,
    }
    return render(request, 'blogSingl.html', context)
