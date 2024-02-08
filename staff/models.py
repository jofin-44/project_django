from django.db import models


# Create your models here.
class staffUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class review(models.Model):
    regno = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    message = models.TextField(blank=False,max_length=250) 
