from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class EditAdminForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'photo', 'bio',]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'au-input au-input--full'}),
            'email': forms.EmailInput(attrs={'class': 'au-input au-input--full'}),
            'bio': forms.TextInput(attrs={'class': 'au-input au-input--full'}),
        }


class AddAdminCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']
