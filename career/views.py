from django.shortcuts import render

from .models import *
from .forms import *


def career(request):
    vacancies = Vacancy.objects.filter(active=True)
    career = Career.objects.first()
    
    # resumeForm = ResumeForm()
    
    # if request.POST:
    #     resumeForm = ResumeForm(request.POST, request.FILES)
        
    #     if resumeForm.is_valid():
    #         obj = resumeForm.save(commit=False)
    #         obj.vacancy = 
    
    context = {
        'vacancies': vacancies,
        'career': career
    }
    return render(request, 'career.html', context)
