from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from staff.models import review
from Admin.models import New_Reg
from django.db import models
from django.db import IntegrityError
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def adminindex(request):
    total_students = User.objects.filter(is_superuser=0 ,is_staff=0).count()
    print(total_students)
    total_staffs = User.objects.filter(is_superuser=0 ,is_staff=1).count()
    print(total_staffs)
    # stdreview = review.objects.all


    return render(request, 'adminhtml/adminindex.html', {'total_students':total_students,'total_staffs':total_staffs})

def adminstaff(request):
    std = review.objects.all()
    return render(request,'adminhtml/adminstaff.html', {'std':std})

def adminstudent(request):
    return render(request,'adminhtml/adminstudent.html')

def newReg(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        reg_no = request.POST.get('Reg_no')
        password = request.POST.get('Pass')

        try:
            # Check if a user with the given username (reg_no) already exists
            existing_user = User.objects.get(username=reg_no)
            msg = f"User with username {reg_no} already exists!"
            return render(request, 'adminindex.html', {'msg': msg})

        except User.DoesNotExist:
            # Create a new user if the username is unique
            my_user = User.objects.create_user(username=reg_no, email=email, password=password,is_superuser=False,is_staff=False)
            my_user.save()

            Regs = New_Reg(
                name=name,
                email=email,
                reg_no=reg_no,
            )
            Regs.save()

            return redirect('login')

        except IntegrityError as e:
            # Handle other integrity errors
            msg = "Error creating user. Please try again!"
            return render(request, 'adminindex.html', {'msg': msg})
    else:

        return render(request, 'adminindex.html')



# def adminviewstd(request):
#     return render(request,'admin/adminviewstd.html')

# def adminviewtr(request):
#     return render(request,'admin/adminviewtr.html')


# --------count of staff and students---------
# views.py
