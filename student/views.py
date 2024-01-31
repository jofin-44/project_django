from django.shortcuts import render, redirect

# Create your views here.

def student(request):
    return render(request,'studenthtml/student.html');

def login(request):
    return render(request, 'studenthtml/login.html');

def registration(request):
    return render(request,'studenthtml/registration.html');



















