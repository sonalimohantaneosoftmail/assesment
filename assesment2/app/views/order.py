from app.models.order import Order
from django.views import View
from django.shortcuts import render

class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        # orders = Order.objects.filter(customer = customer)
        orders=Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'order.html',{'orders':orders})