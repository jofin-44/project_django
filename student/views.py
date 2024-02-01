from django.shortcuts import render, redirect

# Create your views here.

def Home(request):
    return render(request,'Homehtml/Home.html');

def login(request):
    return render(request, 'Homehtml/login.html');

def registration(request):
    return render(request,'Homehtml/registration.html');



















