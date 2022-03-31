from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'title']