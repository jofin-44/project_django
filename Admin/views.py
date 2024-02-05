from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



def adminindex(request):
    return render(request,'admin/adminindex.html')

def adminstaff(request):
    return render(request,'admin/adminstaff.html')

def adminstudent(request):
    return render(request,'admin/adminstudent.html')

# def adminviewstd(request):
#     return render(request,'admin/adminviewstd.html')

# def adminviewtr(request):
#     return render(request,'admin/adminviewtr.html')
