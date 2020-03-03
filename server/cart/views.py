from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from product.models import Product
from rest_framework.response import Response
from .serializer import *
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    if Cart.objects.filter(user=request.user).exists():
        cart = Cart.objects.get(user=request.user)
    else:
        cart = Cart(user=request.user)
    if CartItem.objects.filter(product=product, cart=cart).exists():
        raise serializers.ValidationError({'error': 'this product is already present in your cart'})
    line_total = product.product_price-(product.product_price*(product.product_discount/100))
    cartitem = CartItem(product=product, cart=cart, user=request.user)
    serial = AddToCart(data=request.data)
    if serial.is_valid():
        quantity = serial.validated_data['quantity']
        cartitem.quantity = quantity
        line_total = line_total*quantity
        cartitem.line_total = line_total
        cart.item_count += 1
        cart.total += line_total
        cart.save()
        cartitem.save()
        data = {'success': 'item has been add to your cart'}
    else:
        data = serial.errors
    return Response(data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    if Cart.objects.filter(user=request.user).exists():
        cart = Cart.objects.get(user=request.user)
        if cart.item_count == 0:
            return Response({'error': 'your cart is empty'})
        else:
            cartitem = CartItem.objects.filter(cart=cart)
            data = {}
            for i in range(len(cartitem)):
                data[cartitem[i].product.product_name] = cartitem[i].line_total
            data['item count'] = cart.item_count
            data['total'] = cart.total
            return Response(data)
    else:
        raise serializers.ValidationError({'error': 'your cart does not exist'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, pk):
    cartitem = CartItem.objects.get(pk=pk)
    cart = Cart.objects.get(user=request.user)
    cart.item_count -= 1
    cart.total -= cartitem.line_total
    cart.save()
    cartitem.delete()
    return Response({'success': 'cart item has been removed successfully'})
