from django import template

register = template.Library()



@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    for key in keys:
        if product.id == (int(key)):
            return True    
    return False

@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    keys = cart.keys()
    for key in keys:
        if product.id == (int(key)):
            quantity = cart.get(str(product.id))
            return quantity
    return 0

@register.filter(name="quantity")
def quantity(product , cart):
    # print(type(product.id))
    return cart.get(str(product.id))

@register.filter(name="total")
def total(product, cart):
    # print("quantity======>",quantity(product,cart))
    return quantity(product,cart)*product.price

@register.filter(name="all_total")
def all_total(products , cart):
    sum = 0 
    for product in products:
        sum = sum + total(product,cart)
        # print("==ssss==>",sum)
    return sum

@register.filter(name="currency")
def currency(number):
    return "₹"+str(number)


@register.filter(name="multiply")
def multiply(quantity,price):
    return quantity*price
