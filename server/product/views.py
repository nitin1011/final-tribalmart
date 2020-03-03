from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product
from account.models import Account
from .serializer import ProductSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProduct(request):
    account = Account.objects.get(user=request.user)
    if account.category != 'seller':
        return Response(status=status.HTTP_403_FORBIDDEN)
    product = Product(user=request.user)
    serial = ProductSerializer(product, data=request.data)
    data = {}
    if serial.is_valid():
        serial.save()
        data['success'] = 'create successful'
        return Response(data=data)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if product.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serial = ProductSerializer(product, data=request.data)
    data = {}
    if serial.is_valid():
        serial.save()
        data['success'] = 'update successful'
        return Response(data=data)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
@permission_classes([AllowAny])
def viewProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial = ProductSerializer(product)
    return Response(serial.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNoTExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if product.user != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    operation = product.delete()
    data = {}
    if operation:
        data['delete'] = 'delete successfully'
    else:
        data['delete'] = 'delete fail'
    return Response(data=data)