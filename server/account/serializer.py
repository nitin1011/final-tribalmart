from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account, TempAccount


class userRegistration(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    mobile = serializers.CharField(style={'input_type': 'number'})
    category = serializers.CharField(style={'input_type': 'text'})

    class Meta:
        model = User

        fields = ['username', 'email', 'mobile', 'password', 'password2', 'category']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class VerifyOtp(serializers.ModelSerializer):
    otp = serializers.CharField(style={'input_type': 'number'})

    class Meta:
        model = TempAccount
        fields = ['otp']


class ForgotPassword(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email']


class ResetPassword(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ChangePassword(serializers.ModelSerializer):
    oldpassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['oldpassword', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class EditProfile(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['firstname', 'lastname', 'mobile', 'state', 'city', 'pincode', 'area', 'address']
