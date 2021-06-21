from store.models import offer
# from store.models.offer import Offer
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.offer import Offer
from django.contrib.auth.hashers import check_password, make_password
from django import forms
from store.models import customer


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


# Customer Validation 
def Validatecustomer(customer):
        error_message = None

        if len(customer.username) < 5:
            error_message = "username must be long 5 or  morethan 5!!"
        
        elif len(customer.mobile)<10:
            error_message = "Mobile number must be 10 digit!"

        elif customer.isExists():
            error_message = "Email Address Already Registered..."
        
        elif customer.userExists():
            error_message = "Username already Taken..."


        elif customer.mobileExists():
            error_message = "Mobile Number already Registered..."



        elif len(customer.password) < 6:
            error_message = "password Must be more than 8 character!!"

        # if check.password != check.cpassword :
        #     error_message  =  "password and confirm_password does not match"
                    
        return error_message



# User registration method 
def Registeruser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = make_password(request.POST.get('password'))
        cpassword = make_password(request.POST.get('cpassword'))


        customer = Customer(username=username,
                                email=email,
                                mobile=mobile,
                                password=password,
                                cpassword=cpassword)

        # Hold data when error is occured
        value = {
            'username': username,
            'email': email,
            'mobile': mobile,
        }
        
        error_message = Validatecustomer(customer)

        if not error_message:          
            customer.register() #save data or register user
            messages.success(request, 'Dear {}, Your Account is created Successfully'.format(username))
            return redirect('signin')
        else:
            data = {
                'value': value,
                'error': error_message,
            }

            return render(request, 'signup.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        return Registeruser(request)

# def signin(request):
#     if request.method == 'GET':
#         return render(request, "signin.html")
#     if request.method == 'POST':
#         print("enter 1st step")
#         if Customer.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
#             member = Customer.objects.get(email=request.POST['email'], password=request.POST['password'])
#             print("enter 2nd step")
#             return render(request, 'index.html', {'member': member})
#         else:
#             context = {'msg': 'Invalid username or password'}
#             print("enter 3rd step")
#             return render(request, 'signin.html', context)
#     print("ERROR")
#     return render(request, "signin.html")
def signin(request):
    if request.method == "GET":
        return render(request,'signin.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        client = Customer.get_customer_by_email(email)
        error_message = None
        if client:
            flag = check_password(password,client.password)
            if flag:
                return redirect('index')
                # return redirect('/Dashboard',{"username":username,"email":email})
            else:
                error_message = 'Email Or Password Invalid!!'
        else:
            error_message = 'Email Or Password Invalid!!'
        return render(request,'signin.html',{'error':error_message})


def forgot(request):
    if request.method == 'GET':
        return render(request, "forgot.html")
    email = request.POST.get('email')
    otp = Customer(email=email)
    otp.register()
    messages.success(request,'Send Password in your Registred Email!!')
    return redirect('signin')
