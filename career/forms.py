from django import forms
from .models import *

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'background', 'job_ads', 'tel']


class ResumeForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='UZ')
    )
    
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone_number', 'file']


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'description', 'salary', 'job_type', 'graph', 'duties', 'requirements', 'skills', 'pros', 'active_date', 'active']