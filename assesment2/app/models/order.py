from datetime import datetime
from app.models import customer
from app.models.products import Products
from app.models.customer import Customer
from django.db import models
from app.models.customer import Customer
from app.models.products import Products
import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField()
    address =models.TextField(max_length=500)
    contact =models.IntegerField()
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)


    def __str__(self):
        return self.customer.first_name

    def __str__(self):
        return self.product.name

    
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

