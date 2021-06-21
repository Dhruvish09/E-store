from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

   
    def register(self):
        self.save()
    
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False

    def userExists(self):
        if Customer.objects.filter(username = self.username):
            return True
        return False
    
    def mobileExists(self):
        if Customer.objects.filter(mobile = self.mobile):
            return True
        return False
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def __str__(self):
        return self.username
    