from django.db import models
from django.conf import settings

# Create your models here.


# models.py

from django.db import models

class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)


class Task2(models.Model):
    user        = models.ForeignKey(
                    settings.AUTH_USER_MODEL, 
                    default = 1,
                    null = True,
                    on_delete=models.CASCADE)
  			
    title       = models.CharField(max_length = 255)
    description = models.TextField(max_length = 255)
    length      = models.DecimalField(max_digits = 255, decimal_places=1)
    timer       = models.BigIntegerField(default = 0)