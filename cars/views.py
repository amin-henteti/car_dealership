from django.shortcuts import render

# Create your views here.
from pages.views import data
def cars(request):
    return render(request, 'cars/cars.html', data)
