from django.shortcuts import render

from .models import Member
from cars.models import Car
# Create your views here.
global data
data = {
    'nav_list' : ('HOME', 'CARS', 'SERVICES', 'ABOUT', 'CONTACT'),
}

def home(request):
    featured_cars = Car.objects.order_by('-price').filter(availibility='Sale')
    data2 = {
        'featured_cars': featured_cars,
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