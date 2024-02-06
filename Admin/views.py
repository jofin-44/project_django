from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def adminindex(request):
    total_students = User.objects.filter(is_superuser=0 ,is_staff=0).count()
    print(total_students)
    total_staffs = User.objects.filter(is_superuser=0 ,is_staff=1).count()
    print(total_staffs)

    return render(request, 'adminhtml/adminindex.html', {'total_students':total_students,'total_staffs':total_staffs})

def adminstaff(request):
    return render(request,'adminhtml/adminstaff.html')

def adminstudent(request):
    return render(request,'adminhtml/adminstudent.html')

# def adminviewstd(request):
#     return render(request,'admin/adminviewstd.html')

# def adminviewtr(request):
#     return render(request,'admin/adminviewtr.html')


# --------count of staff and students---------
# views.py
