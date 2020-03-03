from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class AddToCart(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['quantity']
