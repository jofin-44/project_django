from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from staff.models import staffUser,review
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
    if request.method == 'POST':
        regno = request.POST['regno']
        name = request.POST['name'] 
        department = request.POST['department']
        event = request.POST['event']
        message = request.POST['message']
        stdreview = review.objects.create(regno=regno,name=name,department=department,event=event,message=message)
        stdreview.save()
        return redirect('studentreview')
    return render(request,'staffhtml/studentreview.html')

def attendance(request):
    return render(request,'staffhtml/attendance.html')





