from django.db import models

# Create your models here.

class Receipt(models.Model):
    image = models.ImageField(upload_to='img/')
    date = models.DateField(blank=True,null=True)

class Store(models.Model):
    name = models.CharField(max_length=256)

