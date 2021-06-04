from django.db import models
from django.db.models.base import Model

class Offer(models.Model):
    Discount = models.CharField(max_length=10)

    @staticmethod
    def get_all_offers():
        return Offer.objects.all()

    def __str__(self):
        return self.Discount
    
