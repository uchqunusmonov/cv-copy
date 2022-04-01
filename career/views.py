from django.shortcuts import render

from .models import *
from .forms import *


def career(request):
    vacancies = Vacancy.objects.filter(active=True)
    career = Career.objects.all().first()
    
    context = {
        'vacancies': vacancies,
        'career': career
    }
    return render(request, 'career.html', context)
