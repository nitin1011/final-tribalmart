from rest_framework import serializers
from .models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Complaint
        fields = ['orderid', 'complaint']


class ComplaintReply(serializers.ModelSerializer):

    reply = serializers.CharField(style={'input_type': 'text'})
    email = serializers.EmailField()

    class Meta:
        model = Complaint
        fields = ['reply', 'email']
