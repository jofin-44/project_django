from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def staff(request):  # Corrected function name
#     return render(request, 'staffhtml/staffindex.html')

def staff(request):
    return redirect(request,'/staffhtml/staffindex.html')