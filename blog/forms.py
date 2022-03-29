from django import forms
from .models import *


class BlogForm(forms.ModelForm):
    class Meta:
        models = Blog
        fields = ['title', 'text', 'image']
