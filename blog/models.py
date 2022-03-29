from django.db import models
from django.utils.text import slugify


# Create your models here.

class Blog(models.Model):
    slug = models.SlugField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
