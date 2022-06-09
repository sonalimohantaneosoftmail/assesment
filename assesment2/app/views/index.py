from app.models.products import Products
from app.models.category import Category
from django.views import View
from django.shortcuts import render , redirect


class Index(View):
    def get(self, request):
        products = Products.objects.all()
        categories = Category.objects.all()
        category_id = request.GET.get('category')
        # print("category_id",category_id)
        if Category.objects.filter(id = category_id):
            products = Products.objects.filter(category = category_id)
        else:
            products = Products.objects.all()
            for p in products:
                for pm in p.product_image.all():
                    print(pm.image)

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        return render(request , 'index.html',{'products':products,'categories':categories})

    
    def post(self, request):
        product_remove = request.POST.get('product_remove')
        print(product_remove)
        product_id = request.POST.get('product_id')
        print(product_id)
        cart =request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            print("quantity", quantity)
            if quantity:
                if product_remove:
                    if quantity == 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = cart[product_id]-1
                else:
                    cart[product_id] = cart[product_id]+1
            else:
                cart[product_id]=1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print(cart)
        return redirect('index')