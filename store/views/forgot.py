from django.shortcuts import render, redirect
from django.contrib import messages
from store.models.customer import Customer
from django.views import View


class forgot(View):

    def get(self , request):
        return render(request, "forgot.html")
    
    def post(self , request):
        email = request.POST.get('email')
        otp = Customer(email=email)
        otp.register()
        messages.success(request,'Send Password in your Registred Email!!')
        return redirect('signin')
