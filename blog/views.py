from django.shortcuts import render, redirect
from .models import Blog
from .forms import *
from django.core.paginator import Paginator


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
    context = {
        'forms': forms,
    }
    return render(request, 'blogSingl.html', context)
