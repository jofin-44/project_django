from django.db import models
# from django.contrib.auth.models import User


# class SportsRegistration(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     register_number = models.CharField(max_length=20, unique=True)
#     course = models.CharField(max_length=100)
#     event_participating = models.CharField(max_length=100)
#     mail = models.EmailField()

#     def __str__(self):
#         return f"{self.name} - {self.event_participating}"
# Create your models here.
# from django.db import models
# Login = (
#     ("Admin", "Admin"),
#     ("Student", "Student"),
# )

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class contact(models.Model):
    name = models.CharField(blank=False,max_length=50)
    email = models.EmailField(blank=False,max_length=200)
    phone = models.IntegerField(blank=False)
    message = models.TextField(blank=False,max_length=250)    

class support(models.Model):
    name = models.CharField(blank=False,max_length=50)
    email = models.EmailField(blank=False,max_length=200)
    phone = models.IntegerField(blank=False)
    message = models.TextField(blank=False,max_length=250)     
