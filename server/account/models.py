from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default='')
    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    mobile = models.CharField(max_length=10, default='')
    state = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    pincode = models.CharField(max_length=6, default='')
    area = models.CharField(max_length=50, default='')
    address = models.TextField()
    category = models.CharField(max_length=20, default='customer')

    def __str__(self):
        return str(self.username)


class TempAccount(models.Model):
    username = models.CharField(max_length=50, default='')
    firstname = models.CharField(max_length=50, default='')
    lastname = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    mobile = models.CharField(max_length=10, default='')
    password = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    pincode = models.CharField(max_length=6, default='')
    area = models.CharField(max_length=50, default='')
    address = models.TextField()
    category = models.CharField(max_length=20, default='customer')
    shop = models.CharField(max_length=50, default='', blank=True, null=True)
    otp = models.CharField(max_length=10)
    expire = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.username)
