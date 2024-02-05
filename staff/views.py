from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from staff.models import staffUser
# Create your views here.
# Create your views here.
#def Home(request):
 #   return render(request, 'Homehtml/Home.html')

# def staff(request):  # Corrected function name
#     return render(request, 'staffhtml/staffindex.html')

def staffindex(request):
    usr = staffUser.objects.all()
    return render(request,'staffhtml/staffindex.html',{'staffUser':usr})

def timetable(request):
    return render(request,'staffhtml/timetable.html')

def studentreview(request):
    return render(request,'staffhtml/studentreview.html')

def attendance(request):
    return render(request,'staffhtml/attendance.html')





