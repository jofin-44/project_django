from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from student.models import CustomUser
# Create your views here.

# def register(request):
#     errors = {}
#     if request.method == 'POST' :

#         name = request.POST['name'].strip()
#         register_number = request.POST['register_number'].strip()
#         course = request.POST['course'].strip()
#         event_participating = request.POST['event_participating'].strip()
#         mail = request.POST['mail'].strip()



        

def Home(request):
    return render(request,'Homehtml/Home.html')

def aboutview(request):
    return render(request, 'Homehtml/about-us.html')

def userlogin(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        print(username1, password1)
        user = authenticate(request, username=username1, password=password1)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect('baseadmin')
            else:
                login(request,user)
                return redirect('studentindex')  
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'Homehtml/login.html', {'msg': msg})
    return render(request, 'Homehtml/login.html')
        
# def user_logout(request):
#     logout(request)
#     return redirect('user_login')

# def userlogin(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('password')
#         user=authenticate(request,username=username,password=pass1)

#         if user is not None:
#             login(request,user)
#             return render(request, 'Homehtml/Home.html')
#         else:
#             redirect('login')
            
#     return render(request, 'Homehtml/login.html')

# def registration(request):
#     if request.method=='POST':
#         username1=request.POST.get('Name')
#         user_email=request.POST.get('Email')
#         pass1=request.POST.get('Password')

        # my_user=User.objects.create_user(username=username1,email=user_email,password=pass1)
        # my_user.save()

        # Regs=CustomUser(
        #     name=username1,
        #     email=user_email,
        # )
        # Regs.save()
        # return render(request,'Homehtml/Home.html')

    # return render(request,'Homehtml/registration.html')

# views.py
# from django.shortcuts import render, redirect
# from .forms import RegistrationForm, LoginForm
# from .models import CustomUser

# def home(request):
#     return render(request, 'Homehtml/home.html')

# def user_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

        
#         if CustomUser.objects.filter(email=email, password=password).exists():
#             return redirect('home')
#         else:
#             pass

#     return render(request, 'Homehtml/login.html')

# def user_registration(request):
#     if request.method == 'POST':
#         # Handle registration logic here
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Example: Create a new user and redirect to the home page
#             CustomUser.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )
#             return redirect('home')

#     else:
#         form = RegistrationForm()

#     return render(request, 'Homehtml/registration.html', {'form': form})


















