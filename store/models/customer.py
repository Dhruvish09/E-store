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

    def __str__(self):
        return self.username
    