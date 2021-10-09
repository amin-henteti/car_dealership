from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

from .models import Car, MAX_NUMBER_VIEWS
data = {
    'nav_list' : ('HOME', 'CARS', 'SERVICES', 'ABOUT', 'CONTACT'),
}

def gat_views_images(all_cars):
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
    return views_images

def cars(request):
    all_cars = Car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 4)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    views_images = gat_views_images(paged_cars)
                                                
    data2 = {
        'all_cars': paged_cars,
        'views_images': views_images,
    }
    return render(request, 'cars/cars.html', {**data, **data2})

def car_details(request, id):
    car = get_object_or_404(Car, pk=id) #Car.objects.get(id=id)
    car_views_images = { 'carousel-selector-0' : car.main_image.url} # initialize the views_image of the car
    for i in range(MAX_NUMBER_VIEWS) : 
        attr = 'views_images_'+str(i+1) # 0 is reserved for the main image
        view = getattr(car, attr)
        try:
            url = view.url # get the url of an image otherwise throw an error
            if isinstance(url, str): # make sure the url is well defined and not empty or none
                car_views_images['carousel-selector-' + str(i+1)] = url # need this odd looking key for that my version of jinja cant set a variable
        except AttributeError as e:
            print(e)
        except ValueError as ee:
            print(ee)

    data2 = {
        'car': car,
        'car_views_images': car_views_images,
    }
    return render(request, 'cars/car_details.html', {**data, **data2})
