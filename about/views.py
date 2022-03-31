from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about-us.html')

def our_team(request):
    return render(request, 'team.html')


