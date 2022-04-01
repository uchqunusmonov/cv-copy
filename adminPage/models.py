from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='Admin_images/', blank=True)
    bio = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.username