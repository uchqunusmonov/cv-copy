from django import forms
from .models import *


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'image', 'text']

    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'brand', 'image', 'text']