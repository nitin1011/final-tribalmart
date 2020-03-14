from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from complaint.models import Complaint
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complaint_list(request):
    if request.user.is_superuser:
        complaints = Complaint.objects.all()
        data = {}
        for i in complaints:
            data[i.user.username] = i.status
        return Response(data)
    else:
        return Response({'error': 'your do not have permission'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complaint_detail(request, pk):
    if request.user.is_superuser:
        comp = Complaint.objects.get(pk=pk)
        data = {
            'user': comp.user.username,
            'orderid': comp.orderid,
            'complaint': comp.complaint,
            'reply': comp.reply,
            'replied': comp.replied,
            'status': comp.status,
            'date and time': comp.datetime
        }
        return Response(data=data)
    else:
        return Response({'error': 'you can not perform this operation'})
