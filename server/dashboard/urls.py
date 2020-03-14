from django.urls import path
from . import views
urlpatterns = [
    path('complaints', views.complaint_list, name='complaints'),
    path('complaint/<int:pk>', views.complaint_detail, name='complaint-detail'),
]