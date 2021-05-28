from django.db import models
from django.db.models.base import Model

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
