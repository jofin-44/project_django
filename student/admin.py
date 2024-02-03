from django.contrib import admin
from .models import CustomUser
# Register your models here.

class Student(admin.ModelAdmin):
    list_display=('name','email')

admin.site.register(CustomUser,Student)