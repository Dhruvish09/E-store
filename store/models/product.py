from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=1)
    desc = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='media/products/')

    @staticmethod
    def get_all_prodata():
        return Product.objects.all()

    def __str__(self):
        return self.name
    