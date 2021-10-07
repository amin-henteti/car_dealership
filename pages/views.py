from django.shortcuts import render

from .models import Member

# Create your views here.
global data
data = {
    'nav_list' : ('HOME', 'CARS', 'SERVICES', 'ABOUT', 'CONTACT'),
}

def home(request):
    data2 = {
        'members' : Member.objects.all(),
    }
    return render(request, "pages/home.html", {**data, **data2})

def services(request):
    return render(request, "pages/services.html", data)

def about(request):
    data2 = {
        'members': Member.objects.all(),
    }
    return render(request, "pages/about.html", {**data, **data2})

def contact(request):
    return render(request, "pages/contact.html", data)