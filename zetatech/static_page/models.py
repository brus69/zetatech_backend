from django.db import models

# Create your models here.

class Faq(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    img = models.ImageField(upload_to='uploads_team')

    def __str__(self):
        return self.name