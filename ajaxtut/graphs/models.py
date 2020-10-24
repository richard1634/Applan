from django.db import models
from django.conf import settings
# Create your models here.

from django.contrib.postgres.fields import ArrayField


# NOT USING THIS
class Day(models.Model):
  date = models.CharField(max_length = 255)
 # graph = models.ForeignKey(Graph,blank = True,null=True,on_delete=models.CASCADE)
  # gonna need a date and efficiency


class Graph(models.Model):
    user        = models.ForeignKey(
                    settings.AUTH_USER_MODEL, 
                    default = 1,
                    null = True,
                    on_delete=models.CASCADE)
    days = ArrayField(models.CharField(max_length=210), default=list, blank = True)
