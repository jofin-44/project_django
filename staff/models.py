from django.db import models

#---------for attendance------------------------
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Attendance
#---------attendence end-------------------------

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


# ------------------------------------attendance code------------------------------------------------
# def attendance_submit(request):
#     if request.method == 'POST':
#         student_id = request.POST.get('student_id')
#         training = request.POST.get('training')
#         status = request.POST.get('status')
#         date = request.POST.get('date')

#         attendance = Attendance(student_id=student_id, training=training, status=status, date=date)
#         attendance.save()

#         return HttpResponse('Attendance submitted successfully')
#     else:
#         return HttpResponse('Invalid request method')
#-------------------------------------attendance end------------------------------------------------