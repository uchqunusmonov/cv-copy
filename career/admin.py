from django.contrib import admin
from .models import *


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'background', 'job_ads', 'tel']
    

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'job_type', 'graph', 'active']
    
    # def clean(self, *args, **kwargs):
        
    #     print('clean ishladi /////////////////////////') 
    #     print(self)

    #     return self


@admin.register(Resume)
class CvAdmin(admin.ModelAdmin):
    display_fields = ['id', 'name', 'email', 'phone_number', 'file', 'vacancy']
