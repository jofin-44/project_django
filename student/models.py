from django.db import models

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
