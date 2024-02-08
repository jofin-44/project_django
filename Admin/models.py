from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class adminUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class New_Reg(models.Model):
        reg_no=models.CharField(User,max_length=200)
        email=models.CharField(max_length=100)
        name=models.CharField(max_length=200)
        password=models.CharField(max_length=100,null=False)
        c_password=models.CharField(max_length=100,null=True)    
