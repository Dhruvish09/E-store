from django.db import models
from django.db.models.base import Model

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='media/products/')

    def __str__(self):
        return self.name
    