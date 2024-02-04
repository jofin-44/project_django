from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def adminbase(request):
    return render(request,'admin/adminbase.html')

def admindash(request):
    return render(request,'admin/admindash.html')

def adminviewqstn(request):
    return render(request,'admin/adminviewqstn.html')

def adminviewstd(request):
    return render(request,'admin/adminviewstd.html')

def adminviewtr(request):
    return render(request,'admin/adminviewtr.html')
# def register(request):
#     errors = {}
#     if request.method == 'POST' :

#         name = request.POST['name'].strip()
#         register_number = request.POST['register_number'].strip()
#         course = request.POST['course'].strip()
#         event_participating = request.POST['event_participating'].strip()
#         mail = request.POST['mail'].strip()



        


















