from django.shortcuts import render, redirect

# Create your views here.
#def Home(request):
 #   return render(request, 'Homehtml/Home.html')

# def staff(request):  # Corrected function name
#     return render(request, 'staffhtml/staffindex.html')

def staffindex(request):
    return render(request,'staffhtml/staffindex.html')

def timetable(request):
    return render(request,'staffhtml/timetable.html')

def studentreview(request):
    return render(request,'staffhtml/studentreview.html')

def attendance(request):
    return render(request,'staffhtml/attendance.html')





