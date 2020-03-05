from django.urls import path
from . import views

urlpatterns = [
    path('complaint-register', views.complaint_register, name='complaint-register'),
    path('complaint-reply', views.complaint_reply, name='complaint-reply'),
]