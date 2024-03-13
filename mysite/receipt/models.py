from django.db import models

# Create your models here.
#class UploadImage(models.Model):
#    image = models.ImageField(upload_to='img/')

class Receipt(models.Model):
    image = models.ImageField(upload_to='img/')
    date = models.DateField(blank=True,null=True)
