from hashlib import blake2b
from django.db import models
from django.utils.text import slugify
# Create your models here.
from ckeditor.fields import RichTextField


class Brand(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to = 'brand/', blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        slug = f'{self.name}'
        

        self.slug = slugify(slug)

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, blank=True, null=True, related_name='products')
    image = models.ImageField(upload_to = 'products/', blank=True, null=True)
    text = RichTextField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):

        slug = f'{self.brand}-{self.title}'

        self.slug = slugify(slug)

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title