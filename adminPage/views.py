from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate

from .forms import *
from career.forms import *
from career.models import *


def admin_vacancy(request):
    return render(request, 'admin_panel/admin_vacancy.html')


def adminPanel(request, username):
    
    try:
        user = User.objects.get(username=request.user.username)
    except:
        return redirect('login')
        
    
    context = {
        'admin': user 
    }
    
    return render(request, 'admin_panel/index.html', context)    


def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('admin-panel', request.user.username)
    else:
    
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                
                return redirect('admin-panel', user.username)
            else:
                messages.error(request, 'Login or password error')
    
    context = {
    }
    
    return render(request, 'admin_panel/login.html', context)    


def addAdmin(request):
    addAdminCreateForm = AddAdminCreateForm()

    if request.POST:
        addAdminCreateForm = AddAdminCreateForm(request.POST)
        
        if addAdminCreateForm.is_valid():
            obj = addAdminCreateForm.save(commit=False)
            obj.save()
            
            return redirect('login')
    
    context = {
    }
    
    return render(request, 'admin_panel/register.html', context)    


def user_logout(request):
    logout(request)
    
    return redirect('login')


def profile(request, username):
    user = User.objects.get(username=username)

    editAdminForm = EditAdminForm(instance=user)
    
    if request.POST:
        editAdminForm = EditAdminForm(request.POST or None, request.FILES or None, instance=user)
        
        if editAdminForm.is_valid():
            obj = editAdminForm.save(commit=False)
            obj.save()
            
            user = User.objects.get(username=obj.username)
            
            return redirect('profile', user.username)
    
    context = {
        'user': user,
        'editAdminForm': editAdminForm,
    }
    
    return render(request, 'admin_panel/profile.html', context)