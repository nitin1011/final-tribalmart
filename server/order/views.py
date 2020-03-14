from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from cart.models import Cart, CartItem
from rest_framework.response import Response
import random
import string
# Create your views here.


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    try:
        order = Order.objects.get(order_id=the_id)
        id_generator()
    except:
        return the_id


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order(request):
    cart = Cart.objects.get(user=request.user)
    order = Order(customer=request.user)
    cartitems = CartItem.objects.filter(cart=cart)
    subtotal = 0
    shipping = 100
    order.orderid = id_generator()
    order.save()
    data = {'order id': order.orderid}
    j=1
    for i in cartitems:
        orderitem = OrderItem(order=order, product=i.product, price=i.line_total, quantity=i.quantity)

        subtotal += i.line_total
        data[j] = {
                    'product_name': i.product.product_name,
                    'product_price': i.product.product_price,
                    'product_discount': i.product.product_discount,
                    'final_price': i.line_total,
                    'quantity': i.quantity,
                    'shopkeeper': i.product.user.username,
                   }
        j += 1
        orderitem.save()
        i.delete()
    finaltotal = subtotal+shipping
    order.subtotal = subtotal
    order.shipping = shipping
    order.finaltotal = finaltotal
    order.save()
    data['Sub Total'] = subtotal
    data['shipping'] = shipping
    data['Final Total'] = finaltotal
    return Response(data)



