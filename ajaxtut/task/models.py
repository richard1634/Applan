from django.conf import settings
from django.db import models
# Create your models here.



# class Task(models.Model):
#   title       = models.TextField()
#   description = models.TextField()
#   length      = models.TextField()



class Task(models.Model):
    user        = models.ForeignKey(
                    settings.AUTH_USER_MODEL, 
                    default = 1,
                    null = True,
                    on_delete=models.CASCADE)
  			
    title       = models.CharField(max_length = 255)
    description = models.TextField(max_length = 255)
    length      = models.DecimalField(max_digits = 255, decimal_places=1)