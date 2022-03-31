from re import I
from django.contrib import admin
from .models import Blog
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


# Register your models here.

class BlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'id']
    form = BlogAdminForm
    list_display = ('id', 'title', 'get_photo', 'created_at')
    list_display_links = ['title', 'id', 'get_photo']

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'


admin.site.register(Blog, BlogAdmin)
