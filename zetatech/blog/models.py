from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryPost(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=300)
    h1 = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(CategoryPost, on_delete=models.CASCADE)