from tkinter.tix import IMMEDIATE
from django.urls import path
from django.urls.conf import include
from assesment2 import settings
from app.views.index import Index
from app.views.cart import Cart
from app.views.signup import Signup
from app.views.login import Login
from app.views.order import OrderView
from app.views.checkout import Checkout
from app.views.login import Logout
from app.views.payment import payment

urlpatterns = [
    path('',Index.as_view(), name='index'),
    path('cart/',Cart.as_view(), name='cart'),
    path('signup/',Signup.as_view(), name='signup'),
    path('login/',Login.as_view(), name='login'),
    path('order/',OrderView.as_view(), name='order'),
    path('checkout/',Checkout.as_view(), name='checkout'),
    path('logout/',Logout.as_view(), name='logout'),
    path('payment/',payment, name='payment'),

]
