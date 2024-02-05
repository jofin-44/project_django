from django.shortcuts import render

def baseadmin(request):
    return render(request,'admin/baseadmin.html')

def admindash(request):
    return render(request,'admin/admindash.html')

def adminviewqstn(request):
    return render(request,'admin/adminviewqstn.html')

def adminviewstd(request):
    return render(request,'admin/adminviewstd.html')

def adminviewtr(request):
    return render(request,'admin/adminviewtr.html')
