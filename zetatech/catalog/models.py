from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='uploads_icon', blank=True)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.CharField(max_length=300, blank=True)
    h1 = models.CharField(max_length=50, blank=True)
    mini_content = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    pup_date = models.DateField(auto_now_add=True)
    h2 = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    catalog = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, 
                                related_name='products', null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = 0
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title