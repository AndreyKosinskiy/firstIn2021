from django.shortcuts import redirect, render

# Create your views here.


def login(request):
    if request.method == 'POST':
        return redirect('register')
    else:
        return render(request, 'accounts/login.html')

def logout(request):

    return render(request, 'accounts/register.html')


def register(request):
    if request.method == 'POST':

        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
