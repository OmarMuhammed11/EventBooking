from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField(default= 0.0)
    edition = models.IntegerField(default= 1)
    
# Create your models here.
