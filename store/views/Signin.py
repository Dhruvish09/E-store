from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password, make_password
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session

class Signin(View):

    def get(self , request):
        return render(request, 'signin.html')
    
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        try:
            flag = check_password(password , customer.password)
            login(request , flag)
            request.session['email'] = email
            return redirect('index')
        except:
            return render(request,'index.html')
         

        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # customer = Customer.get_customer_by_email(email)
        # error_message = None
        # if customer:
        #     flag = check_password(password , customer.password)
        #     if flag:
        #         login(request )
        #         request.session['email'] = email
        #         return redirect('index')
        #     else:
        #         error_message = 'Email or Password is Invalid!'
        
        # else:
        #     error_message = 'Email or Password Invalid!'

        # return render(request , 'signin.html', {'error' : error_message})