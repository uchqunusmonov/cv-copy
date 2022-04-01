from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate

from .forms import *


def adminPanel(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
        
    
    context = {
    }
    
    return render(request, 'admin_panel/index.html', context)    


def user_login(request):
    userLoginForm = UserLoginForm()
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            
            return redirect('admin-panel')
        else:
            messages.error(request, 'Login or password error')
    
    context = {
    }
    
    return render(request, 'admin_panel/login.html', context)    