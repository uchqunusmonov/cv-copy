from django.db import models

from ckeditor.fields import RichTextField

# from django.contrib.contenttypes.fields import GenericRelation
# from hitcount.models import HitCount

from phonenumber_field.modelfields import PhoneNumberField

from adminPage.models import User


class Career(models.Model):
    name = models.CharField(max_length=500)
    background = models.ImageField(upload_to='Career/images/')
    job_ads = models.TextField(verbose_name='Job advertisement title')
    tel = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return self.name


class Vacancy(models.Model):
    JOB_CHOICES = [
        ('online', 'online'),
        ('offline', 'offline')
    ]
    
    GRAPH = [
        ('full time', 'full time'),
        ('part time', 'part time'),
    ]

    name = models.CharField(max_length=100)
    description = RichTextField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    salary = models.PositiveIntegerField(help_text='enter the currency in dollars', default=0)
    job_type = models.CharField(max_length=10, choices=JOB_CHOICES)
    graph = models.CharField(max_length=10, choices=GRAPH, default='full time')
    active_date = models.DateField(blank=True, null=True)
    duties = models.CharField(max_length=500, blank=True)
    requirements = models.CharField(max_length=500, blank=True)
    pros = models.CharField(max_length=500, blank=True)
    skills = models.CharField(max_length=500, blank=True)
    active = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class Resume(models.Model):
    # statusResume = [
    #     ('')    
    # ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    file = models.FileField(help_text='Send your resume as a file')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(auto_now_add=True)
    # status = models.CharField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

