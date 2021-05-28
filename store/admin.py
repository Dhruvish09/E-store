from django.contrib import admin

from store.models import category
from .models.product import Product
from store.models.category import Category


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
