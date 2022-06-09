from django.db import models
from app.models.products import Products

class Product_images(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='product_image')
    image =models.ImageField(upload_to = "upload/pictures/")
    