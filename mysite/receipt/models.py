from django.db import models

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
    store_id = models.ForeignKey(Store,on_delete=models.SET_NULL,null=True)

class Item(models.Model):
    receipt_id = models.ForeignKey(Receipt,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    qty = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

