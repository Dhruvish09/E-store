from django.shortcuts import render
from .models.product import Product
from .models.category import Category


# Create your views here.
def index(request):
    products = Product.get_all_prodata()
    categorys = Category.get_all_catdata()
    return render(request,'index.html',{'products':products,'categorys':categorys})


