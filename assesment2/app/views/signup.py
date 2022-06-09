from django.views import View
from django.shortcuts import render , redirect
from app.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Signup(View):
    def get(self, request):
        return render(request,"signup.html")


    def post(self, request):
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        data={
            'first_name':f_name,
            'last_name':l_name,
            'email':email,
            'phone':phone,
        }

        customer = Customer(first_name = f_name , last_name = l_name, email = email , phone = phone, password = password)
        error_msg = self.customer_validation(customer)
        if error_msg == None:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('login')
        return render(request , 'signup.html',{'error':error_msg,'data1':data})


    def customer_validation(self, customer2):
        error_msg = None
        if not(customer2.first_name):
            error_msg = "First name is not available"
        elif len(customer2.first_name)<=3:
            error_msg = "First name should be > 3"
        elif not(customer2.last_name):
            error_msg = "Last name is not available"
        elif len(customer2.last_name)<=3:
            error_msg = "Last name should be > 3"
        elif not(customer2.email):
            error_msg = "Email is not available"
        elif len(customer2.email)<=13:
            error_msg = "Email should be > 13"
        elif not(customer2.phone):
            error_msg = "Phone is not available"
        elif len(customer2.phone)<=9:
            error_msg = "Phone should be > 9"
        elif not(customer2.password):
            error_msg = "Password is not available"
        elif len(customer2.password)<=3:
            error_msg = "Password should be > 3"
        elif customer2.is_exists():
            error_msg = "This email already exists"

        return error_msg
        


        
