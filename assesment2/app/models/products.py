from email.mime import image
from django.db import models
from app.models.category import Category

class Products(models.Model):
    name = models.CharField(max_length=50)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    description =models.CharField(max_length=100)
    price =models.IntegerField()

    
    def __str__(self):
        return self.name
    
    


