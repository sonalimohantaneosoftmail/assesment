from django.db import models
from django.shortcuts import render
from django.contrib.auth.hashers import check_password

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)


    # for signup
    def is_exists(self):
        if Customer.objects.filter(email= self.email):
            return True
        else:
            return False


    # for login
    @staticmethod
    def customer_validation(email1):
        try:
            user = Customer.objects.get(email = email1)
        except:
            user = None
        return user
