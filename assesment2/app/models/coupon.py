from django.db import models
import uuid
from app.models.products import Products
import shortuuid


def random_code():
    return shortuuid.ShortUUID().random(length=6).upper()

class Coupon(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    active=models.BooleanField(default=True)
    discount = models.IntegerField()
    product= models.ForeignKey(Products,on_delete=models.CASCADE,related_name='coupons')
    code = models.CharField(max_length=6,unique=True,null=False,default=random_code)