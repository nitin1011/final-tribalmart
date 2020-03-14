from rest_framework import serializers
from .models import Product, Review


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name', 'product_category', 'product_price', 'product_discount',
                  'product_image', 'product_disc']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['rating', 'comment']
