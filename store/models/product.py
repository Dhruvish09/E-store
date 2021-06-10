from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields.related import ManyToManyField
from .category import Category
from .offer import Offer
from store.models import offer

class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    offerprice = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default=None)
    offer = models.ForeignKey(Offer , on_delete=models.CASCADE , default='',blank=True,null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='media/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();
        
    @staticmethod
    def get_all_products_by_offerid(offer_id):
        if offer_id:
            return Product.objects.filter(offer = offer_id)
        else:
            return Product.get_all_products();
        
    # def __str__(self):
    #     return self.price + 'Rs'
    
