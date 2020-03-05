from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Complaint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orderid = models.CharField(max_length=100, default='')
    complaint = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.datetime)
