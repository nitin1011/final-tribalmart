from apscheduler.schedulers.background import BackgroundScheduler
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializer import *
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings
from .models import TempAccount, Account
import base64
from datetime import datetime, timedelta, timezone
import secrets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from random import random
# Create your views here.


def get_otp():
    otp = int(random()*1000000)
    try:
        temp = TempAccount.objects.get(otp=otp)
    except:
        temp = None
    if temp is not None:
        get_otp()
    else:
        return otp


@api_view(['GET', ])
@renderer_classes([TemplateHTMLRenderer])
@permission_classes((AllowAny, ))
def register(request):
    serial = userRegistration(data=request.data)
    if serial.is_valid():
        otp = get_otp()
        p1 = serial.validated_data['password']
        p2 = serial.validated_data['password2']
        username = serial.validated_data['username']
        email = serial.validated_data['email']
        mobile = serial.validated_data['mobile']
        category = serial.validated_data['category']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'user with same email address already exists '})
        if Account.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError({'mobile': 'user with same mobile no. already exists '})
        if p1 != p2:
            raise serializers.ValidationError({'password': 'password does not match'})
        password = base64.b64encode(p1.encode("utf-8"))
        password = str(password)
        password = password[2:len(password)-1]
        ex = datetime.now()+timedelta(seconds=300)
        temp = TempAccount(username=username, email=email, mobile=mobile,
                           otp=otp, password=password, expire=ex, category=category)

        temp.save()
        subject = 'Tribalmart verification mail'
        message = 'Welcome to Tribalmart\nplease enter this otp to verify your email\n'+str(otp)+''
        from_email = settings.EMAIL_HOST_USER
        tolist = [serial.data['email']]

        send_mail(subject, message, from_email, tolist)

        data = {'verify': 'verify your email'}
    else:
        data = serial.errors
    return Response(data, template_name='index.html')


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    serial = VerifyOtp(data=request.data)
    if serial.is_valid():
        print(serial.data['otp'])
        try:
            temp = TempAccount.objects.get(otp=serial.data['otp'])
        except:
            temp = None
        data = {}
        if temp is not None:
            password = base64.b64decode(temp.password).decode("utf-8")
            user = User.objects.create_user(username=temp.username, email=temp.email, password=password)
            user.save()
            account = Account(user=user, username=temp.username, email=temp.email, mobile=temp.mobile,
                              category=temp.category)
            account.save()
            temp.delete()

            data['register'] = 'you have been registered successfully'
            data['username'] = user.username
            data['email'] = user.email
        else:
            data['otp'] = 'Invalid OTP'
    else:
        data = serial.errors
    return Response(data)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_otp, 'interval', seconds=300)
    scheduler.add_job(check_token, 'interval', hours=20)
    scheduler.start()


def check_otp():
    temp = TempAccount.objects.all()
    for i in temp:
        dt = datetime.now()
        dt = dt.replace(tzinfo=timezone.utc)
        if i.expire < dt:
            i.delete()


def check_token():
    token = Token.objects.all()
    for i in token:
        if len(str(i.key)) == 14:
            if i.created+timedelta(days=1) < datetime.now().replace(tzinfo=timezone.utc):
                i.delete()


@api_view(['GET', ])
@renderer_classes([TemplateHTMLRenderer])
@permission_classes((AllowAny, ))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        token = Token.objects.create(user=user)

        return Response({'login': 'login successfully',
                         'token': token.key
                         })
    else:
        return Response({'login': 'error in login'}, template_name='index.html')


@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    auth.logout(request)
    return Response({'logout': 'logout successfully'})

@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    serial = ForgotPassword(data=request.data)
    if serial.is_valid():
        email = serial.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user is not None:
            token = Token(key=secrets.token_urlsafe(10), user_id=user.id)
            token.save()
        else:
            raise serializers.ValidationError({'email': 'user with the email address not exist '})

        subject = 'Tribalmart Mail'
        message = 'Please click the below link to reset your password \nhttp://localhost:8000/account/reset/'+str(token)
        from_email = settings.EMAIL_HOST_USER
        tolist = [email]
        send_mail(subject, message, from_email, tolist)
        data = {'reset': 'reset password'}
    else:
        data = serial.errors
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reset_password(request, token):
    serial = ResetPassword(data=request.data)
    if serial.is_valid():
        p1 = serial.validated_data['password']
        p2 = serial.validated_data['password2']
        if p1 != p2:
            raise serializers.ValidationError({'error': 'password does not match'})
        else:
            user = request.user
            user.set_password(p1)
            user.save()
            data = {'reset': 'password reset successfully'}
            tok = Token.objects.get(user=user)
            tok.delete()
    else:
        data = serial.errors
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serial = ChangePassword(data=request.data)
    data={}
    if serial.is_valid():
        oldp = serial.validated_data['oldpassword']
        p1 = serial.validated_data['password']
        p2 = serial.validated_data['password2']
        user = auth.authenticate(username=request.user.username, password=oldp)
        if request.user == user:
            if p1 == p2:
                user.set_password(p1)
                user.save()
                data = {'success': 'password changed successfully'}
            else:
                raise serializers.ValidationError({'error': 'password do not match'})
        else:
            raise serializers.ValidationError({'user': 'old password is incorrect'})
    else:
        data = serial.errors
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    account = Account.objects.get(user=request.user)
    serial = EditProfile(data=request.data)
    if serial.is_valid():
        account.firstname = serial.validated_data['firstname']
        account.lastname = serial.validated_data['lastname']
        mobile = serial.validated_data['mobile']
        account.state = serial.validated_data['state']
        account.city = serial.validated_data['city']
        account.pincode = serial.validated_data['pincode']
        account.area = serial.validated_data['area']
        account.address = serial.validated_data['address']

        if account.mobile != mobile and Account.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError({'error': 'user with this mobile number is already exists'})
        account.mobile = mobile
        account.save()
        data = {'success': 'your profile has been updated successfully'}
    else:
        data = serial.errors
    return Response(data)

