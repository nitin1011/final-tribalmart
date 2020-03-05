from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import send_mail
from .models import Complaint
from rest_framework.response import Response
from .serializer import ComplaintSerializer, ComplaintReply
from django.conf import settings
from account.models import *
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complaint_register(request):
    serial = ComplaintSerializer(data=request.data)
    if serial.is_valid():
        orderid = serial.validated_data['orderid']
        complaint = serial.validated_data['complaint']
        user = request.user

        comp = Complaint(user=user, orderid=orderid, complaint=complaint)
        comp.save()
        return Response({'success': 'your complaint has been registered successfully'})
    else:
        return Response(serial.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complaint_reply(request):
    account = Account.objects.get(user=request.user)
    if account.category == 'cra':
        serial = ComplaintReply(data=request.data)
        if serial.is_valid():
            reply = serial.validated_data['reply']
            email = serial.validated_data['email']
            subject = 'Complaint Reply'
            message = reply
            from_email = settings.EMAIL_HOST_USER
            tolist = [email]

            send_mail(subject, message, from_email, tolist)
            user = User.objects.get(email=email)
            comp = Complaint.objects.get(user=user)
            comp.delete()
            return Response({'success': 'reply has been send'})
        else:
            return Response(serial.errors)
    else:
        return Response({'error': 'your are not permitted to do this action'})
