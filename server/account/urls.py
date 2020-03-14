from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('otp', views.verify_otp, name='otp'),
    path('forgot', views.forgot_password, name='forgot'),
    path('reset/<str:token>', views.reset_password, name='reset'),
    path('change_password', views.change_password, name='change-password'),
    path('edit-profile', views.edit_profile, name='edit-profile'),
]