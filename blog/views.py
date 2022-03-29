from django.shortcuts import render, redirect
from .models import Blog
from .forms import *

# Create your views here.

def blog(request):
    form = Blog.objects.all()
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
    }
    return render(request, 'base.html', context)