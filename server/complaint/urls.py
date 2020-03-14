from django.urls import path
from . import views

urlpatterns = [
    path('complaint-register', views.complaint_register, name='complaint-register'),
    path('complaint-reply/<int:pk>', views.complaint_reply, name='complaint-reply'),
]