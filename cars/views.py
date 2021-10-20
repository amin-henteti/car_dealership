from io import SEEK_SET
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models.query import QuerySet
from django.db.models.sql.datastructures import Join
from itertools import chain

# Create your views here.

from .models import Car, MAX_NUMBER_VIEWS

CARS_PER_PAGE = 4

data = {
    "nav_list": ("HOME", "CARS", "SERVICES", "ABOUT", "CONTACT"),
}

home_search_fields = ("title", "model", "location", "year")
fields_values = {
    field: Car.objects.values_list(field, flat=True).distinct()
    for field in home_search_fields
}


def gat_views_images(all_cars):
    views_images = {}
    for car in all_cars:
        # initialize the views_image of a certain car indexed by a the id in the database
        views_images[car.id] = []
        for i in range(MAX_NUMBER_VIEWS):
            attr = "views_images_" + str(i + 1)  # 0 is for the main image in a way
            view = getattr(car, attr)
            try:
                # get the url of an image otherwise throw an error
                url = view.url
                # make sure the url is well defined and not empty or none
                if isinstance(url, str):
                    views_images[car.id].append(url)
            except AttributeError as e:
                print(e)
            except ValueError as ee:
                print(ee)
    return views_images


def cars(request):

    all_cars = Car.objects.order_by("-created_date")
    paginator = Paginator(all_cars, CARS_PER_PAGE)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    views_images = gat_views_images(paged_cars)

    data2 = {
        "all_cars": paged_cars,
        "views_images": views_images,
        "search_fields": fields_values,
    }
    return render(request, "cars/cars.html", {**data, **data2})


def car_details(request, id):
    car = get_object_or_404(Car, pk=id)  # Car.objects.get(id=id)
    # initialize the views_image of the car
    car_views_images = {"carousel-selector-0": car.main_image.url}
    for i in range(MAX_NUMBER_VIEWS):
        attr = "views_images_" + str(i + 1)  # 0 is reserved for the main image
        view = getattr(car, attr)
        try:
            # get the url of an image otherwise throw an error
            url = view.url
            # make sure the url is well defined and not empty or none
            if isinstance(url, str):
                # need this odd looking key for that my version of jinja cant set a variable
                car_views_images["carousel-selector-" + str(i + 1)] = url
        except AttributeError as e:
            print(e)
        except ValueError as ee:
            print(ee)

    data2 = {
        "car": car,
        "car_views_images": car_views_images,
    }
    return render(request, "cars/car_details.html", {**data, **data2})


def search(request):

    all_cars = Car.objects.order_by("-created_date")
    filter_cars = None
    for field_name in home_search_fields:
        field_value = request.GET.get(field_name)
        if not (field_value is None):
            cars_fields = (
                [field_name]
                if field_name != "keyword"
                else [
                    "availibility",
                    "body_style",
                    "color",
                    "condition",
                    "description",
                    "engine",
                    "features",
                    "fuel_type",
                    "transmission",
                    "location",
                    "model",
                    "provinance",
                    "title",
                    "year",
                ]
            )
            if filter_cars is None:
                cond = {cars_fields[0] + "__icontains": field_value}
                # initialisation, QuerySet(Car) doesnt work to make an empty query
                filter_cars = all_cars.filter(**cond)
            print(55 * "-", cars_fields)
            # in the keyword case we make search in multiple fields with union condition (OR)
            if field_name == "keyword":
                for field in cars_fields:
                    cond = {field + "__icontains": field_value}
                    if filter_cars is None:
                        q = all_cars.filter(**cond)  # A filter from all cars query
                    # update the search by joining the query with the previous ones
                    filter_cars = filter_cars | q
            else:
                filter_cars = filter_cars.filter(
                    **{cars_fields[0] + "__icontains": field_value}
                )
    if filter_cars is None:  # No applied filters
        filter_cars = all_cars
    paginator = Paginator(filter_cars, CARS_PER_PAGE)
    page = request.GET.get("page")
    paged_cars = paginator.get_page(page)
    views_images = gat_views_images(paged_cars)

    data2 = {
        "all_cars": paged_cars,
        "views_images": views_images,
        "search_fields": fields_values,
    }
    return render(request, "cars/search.html", {**data, **data2})
