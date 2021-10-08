from django.shortcuts import render

from .models import Member
from cars.models import Car, MAX_NUMBER_VIEWS
# Create your views here.
global data
data = {
    'nav_list' : ('HOME', 'CARS', 'SERVICES', 'ABOUT', 'CONTACT'),
}

def home(request):
    featured_cars = Car.objects.order_by('-price').filter(availibility='Sale')
    all_cars = Car.objects.order_by('-created_date')
    views_images = {}
    for car in all_cars:
        views_images[car.id] = [] # initialize the views_image of a certain car indexed by a the id in the database
        for i in range(MAX_NUMBER_VIEWS) : 
            attr = 'views_images_'+str(i+1) # 0 is for the main image in a way
            view = getattr(car, attr)
            try:
                url = view.url # get the url of an image otherwise throw an error
                if isinstance(url, str): # make sure the url is well defined and not empty or none
                    views_images[car.id].append(url)
            except AttributeError as e:
                print(e)
            except ValueError as ee:
                print(ee)
                                                
    data2 = {
        'views_images': views_images,
        'featured_cars': featured_cars,
        'members' : Member.objects.all(),
        'all_cars': all_cars,
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