from django.contrib.auth.hashers import check_password
from app.models.customer import Customer
from django.views import View
from django.shortcuts import render , redirect


class Login(View):
    def get(self, request):
        return render(request , 'login.html')

    def post(self,request):

        email1= request.POST.get('email')
        password1 = request.POST.get('password')
        user = Customer.customer_validation(email1)
        error_msg = None
        if user:
            if check_password(password1,user.password):
                request.session['customer'] = user.id
                return redirect('index')
            else:
                error_msg = "Invalid username and password"
        else:

            error_msg = "Invalid username and password"
        return render(request, "login.html",{'error':error_msg})

class Logout(View):
    def get(self , request):
        request.session.clear()
        return redirect('login')














        # email1= request.POST.get('email')
        # password = request.POST.get('password')
        # user= Customer.customer_validation(email1)
        # error_msg = None
        # if user:
        #     if check_password(password,user.password):
        #         request.session['customer'] = user.id
        #         return redirect('index')
        #     else:
        #         error_msg = "invalid username and password"
        # else:
        #     error_msg = "invalid username and password"
        # return render(request, "login.html",{'error':error_msg})








        # email1 = request.POST.get('email')
        # password1 = request.POST.get('password')
        # user = Customer.customer_exists(email1)
        # error_msg = None
        # if user:
        #     if check_password(password1,user.password):
        #         request.session['customer'] = user.id
        #         return redirect('index')
        #     else:
        #         error_msg = "invalid user_name and password"
        # else:
        #     error_msg = "invalid user_name and password"
        # return render(request , 'login.html', context={'error':error_msg})