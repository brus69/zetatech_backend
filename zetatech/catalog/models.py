from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    slug = models.SlugField()

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=300)
    h1 = models.CharField(max_length=50)
    mini_content = models.TextField()
    price = models.IntegerField()
    pup_date = models.DateField()
    h2 = models.CharField(max_length=100)
    content = models.TextField()
    catalog = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')