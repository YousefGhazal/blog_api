from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(max_length=250, unique=True, populate_from="title")
    description = models.TextField(max_length=250)
        
    body = RichTextField(max_length=None)
    published = models.DateTimeField(auto_now_add=True)
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
        
    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published']),
            ]
        
    def __str__(self):
        return self.title
    