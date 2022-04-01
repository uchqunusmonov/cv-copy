from django import forms
from .models import *


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']