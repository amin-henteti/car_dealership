from django.shortcuts import render

from .models import Member
from cars.models import Car, MAX_NUMBER_VIEWS
from cars.views import gat_views_images, data, fields_values

# Create your views here.


def home(request):
    featured_cars = Car.objects.order_by("-price").filter(availibility="Sale")
    all_cars = Car.objects.order_by("-created_date")
    views_images = gat_views_images(all_cars)
    data2 = {
        "featured_cars": featured_cars,
        "all_cars": all_cars,
        "views_images": views_images,
        "members": Member.objects.all(),
        "search_fields": fields_values,
    }
    return render(request, "pages/home.html", {**data, **data2})


def services(request):
    return render(request, "pages/services.html", data)


def about(request):
    data2 = {
        "members": Member.objects.all(),
    }
    return render(request, "pages/about.html", {**data, **data2})


def contact(request):
    return render(request, "pages/contact.html", data)
