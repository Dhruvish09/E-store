from store.models import offer
# from store.models.offer import Offer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.offer import Offer
from django.contrib.auth.hashers import check_password, make_password
from django import forms
from store.models import customer
from django.views import View


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
# def signin(request):
    # if request.method == "GET":
        # return render(request,'signin.html')
    # else:
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # client = Customer.get_customer_by_email(email)
        # error_message = None
        # if client:
            # flag = check_password(password,client.password)
            # if flag:
                # return redirect('index')
                # # return redirect('/Dashboard',{"username":username,"email":email})
            # else:
                # error_message = 'Email Or Password Invalid!!'
        # else:
            # error_message = 'Email Or Password Invalid!!'
        # return render(request,'signin.html',{'error':error_message})

# def signin(request):
#     if request.method == 'GET':
#         return render(request, 'signin.html')

#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('index')
#     else:
#         return render(request, 'signin.html')
