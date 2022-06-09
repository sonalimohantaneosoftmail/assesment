from django.views import View
from django.shortcuts import render , redirect
from app.models.products import Products


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        keys = cart.keys()
        products = Products.objects.filter(id__in = keys)
        return render(request, "cart.html",{'products':products})










    # def get(self, request):
    #     cart = request.sesson.get('cart')
    #     keys = cart.keys()
    #     products = Products.objects.filter(id__in = keys) 
    #     return render(request , 'cart.html', {'products':products})