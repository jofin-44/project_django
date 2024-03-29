"""
URL configuration for sportsmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import path
#from student.views import Home, login
from staff.views import staffindex, timetable, studentreview, attendance
from Admin.views import adminindex,adminstaff,adminstudent
from student.views import Home, userlogin, studentindex, studentattendance, studentsupport, studentregform,aboutview,logout_views, AboutUs, Achievements, upcominggames
# from Admin.views import baseadmin,admindash,adminviewqstn,adminviewstd,adminviewtr
# from student.views import Home, userlogin, aboutview
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('registration', registration, name='registration'),
    path('',Home,name='Home'),
    path('login',userlogin, name='login'),
    path('logout',logout_views, name='logout'),
    path('aboutus', aboutview, name='aboutus'),
    path('AboutUs', AboutUs, name='AboutUs'),
    path('Achievements',Achievements, name='achievements'),
    path('upcominggames',upcominggames,name='Upcominggames'),


    # staff urls here
    path('staffindex', staffindex, name="staffindex"),
    path('timetable', timetable, name="timetable"),
    path('studentreview', studentreview, name="studentreview"),
    path('attendance', attendance, name="attendance"),

    #admin urls here


    path('adminindex',adminindex,name='adminindex'),
    path('adminstaff',adminstaff,name='adminstaff'),
    path('adminstudent',adminstudent,name='adminstudent'),
   
    
    # path('registration', registration, name='registration'),

    # student urls here
    path('studentindex/',studentindex, name="studentindex"),
    path('studentattendance', studentattendance, name="studentattendance"),
    path('studentsupport', studentsupport, name="studentsupport"),
    path('studentregform', studentregform, name="studentregform"),
         
 


]
