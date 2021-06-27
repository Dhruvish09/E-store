from store.models import offer
# from store.models.offer import Offer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from store.models.product import Product 
from store.models.category import Category 
from store.models.offer import Offer
from django.contrib.auth.hashers import check_password, make_password
from django import forms
from store.models import customer
from django.views import View


# Create your views here.
def index(request):
    products = None

    offers = Product.objects.order_by('-offer')
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    offers = Offer.get_all_offers()   
    offerID = request.GET.get('offer')
    if offerID:
        products = Product.get_all_products_by_offerid(offerID)
    else:
        pass

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['offers'] = offers
    return render(request, 'index.html', data)
