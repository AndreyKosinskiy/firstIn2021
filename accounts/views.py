from django.shortcuts import redirect, render

# Create your views here.
def login(request):
   return redirect('index')

def logout(request):
    return render(request,'accounts/register.html')

def register(request):
    return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')