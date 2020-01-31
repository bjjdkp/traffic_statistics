from django.db import models

# Create your models here.

from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)


class TrafficInfo(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=10)
    down_byte = models.CharField(max_length=50)



