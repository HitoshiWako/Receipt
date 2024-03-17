from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=256)
    branch = models.CharField(max_length=256,blank=True, null=True)
    def __str__(self) -> str:
        if self.branch:
            return self.name +' - '+self.branch
        return self.name

class Receipt(models.Model):
    image = models.ImageField(upload_to='img/')
    date = models.DateField(blank=True,null=True)
    store = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)

