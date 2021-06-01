from django.shortcuts import render, redirect
from django.contrib import messages
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import check_password, make_password
from django import forms
from store.models import customer


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signin(request):
    return render(request, "signin.html")


def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = make_password(request.POST.get('password'))
        cpassword = make_password(request.POST.get('cpassword'))
        hashedPassword = make_password(password=password)

        customer = Customer(username=username,
                                email=email,
                                mobile=mobile,
                                password=hashedPassword,
                                cpassword=hashedPassword)

        # Hold data when error is occured
        value = {
            'username': username,
            'email': email,
            'mobile': mobile,
        }

        # Validation 
        error_message = None

        if len(username) < 5:
            error_message = "username must be long 5 or  morethan 5!!"

        elif customer.isExists():
            error_message = "Email Address Already Registered..."

        elif len(mobile) < 10:
            error_message = "Please enter 10 digit of your mobile number!!"

        elif len(password) < 6:
            error_message = "password Must be more than 8 character!!"

        elif password != cpassword:
            error_message = "Please enter both password same!"


        if not error_message:
            
            customer.register()
            messages.success(request, 'Dear {}, Your Account is created Successfully'.format(username))
            return redirect('signin')
        else:
            data = {
                'value': value,
                'error': error_message,
            }

            return render(request, 'signup.html', data)


def final_reg(request):
    return render(request, 'final_reg.html')


def final_log(request):
    return render(request, 'final_log.html')
