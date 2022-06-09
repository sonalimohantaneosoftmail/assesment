from django.contrib import admin
from app.models.category import Category
from app.models.customer import Customer
from app.models.order import Order
from app.models.products_images import Product_images
from app.models.products import Products
from django.utils.html import format_html
from app.models.coupon import Coupon

# Register your models here.
class ProductConfiguration(admin.ModelAdmin):
    list_display = ['name','category','description','price']

    # def image(self,obj):
    #     return format_html(f"""
    #     <a target='_blank' href='{obj.image.url}'><img height='50px' src='{obj.image.url}'></a> """)

admin.site.register(Category)
admin.site.register(Customer)   
admin.site.register(Order)
admin.site.register(Product_images)
admin.site.register(Products,ProductConfiguration)
admin.site.register(Coupon)
