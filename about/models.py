from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Information(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    text = RichTextField()
    image = models.ImageField(upload_to='information/')
    back_ground =  models.ImageField(upload_to='background/', blank=True, null=True)
    warehouse = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Sphere(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    text = RichTextField()


    def __str__(self) -> str:
        return self.title

class OurTeam(models.Model):
    image = models.ImageField(upload_to='OurTeam/', blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    position = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    responsibility = models.CharField(max_length=250, blank=True, null=True)
    experience = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    fax = models.PositiveBigIntegerField(blank=True, null=True)


    def __str__(self) -> str:
        return self.first_name
