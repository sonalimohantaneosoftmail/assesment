from calendar import c
import code
from app.templatetags.filter_tags import quantity
from app.models.customer import Customer
from app.models.products import Products
from app.models.order import Order
from django.views import View
from django.shortcuts import render , redirect
from app.models.coupon import Coupon


class Checkout(View):
    def get(self, request):
        return redirect('cart')

    def post(self , request):
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        coupon = request.POST.get('coupon')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')

        sum=0
        for k,v in cart.items():
            print(k,v)
            print(type(k),type(v))
            pro = Products.objects.get(id=int(k))
            print(pro.price*v)
            sum = sum +(pro.price*v)
        print(sum)

        keys = cart.keys()
        sub_total_after_discount = 0
        if coupon is not None:
            coupon = Coupon.objects.get(code=coupon)
            discount = coupon.discount
            sub_total_after_discount = sum * (discount/100)

            # return render(request,"test-payment.html")

        products = Products.objects.filter(id__in = keys)
        for product in products:
            Order(
                customer = Customer(id = customer_id),
                product = product,
                price = product.price,
                quantity = cart.get(str(product.id)),
                address = address,
                contact = contact
            ).save()
        request.session['cart']={}
        return render(request,"order.html")