from django.shortcuts import redirect, render

# Create your views here.

def register(request):
    if request.method == 'POST':
        print('this was a post request')
        return redirect('login')
    return render(request, 'account/register.html')

def login(request):
    return render(request, 'account/login.html')

def logout(request):
    return redirect("home")


def dashboard(request):
    return render(request, 'account/dashboard.html')

