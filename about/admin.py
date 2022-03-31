from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Information)
class AdminInformation(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Sphere)
class AdminSphere(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(OurTeam)
class AdminOurTeam(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name']