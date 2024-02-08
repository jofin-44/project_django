from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def adminindex(request):
    return render(request,'adminhtml/adminindex.html')

def adminstaff(request):
    return render(request,'adminhtml/adminstaff.html')

def adminstudent(request):
    return render(request,'adminhtml/adminstudent.html')

# def adminviewstd(request):
#     return render(request,'admin/adminviewstd.html')

# def adminviewtr(request):
#     return render(request,'admin/adminviewtr.html')
