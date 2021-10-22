from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User

from carwebsite.settings import EMAIL_HOST_USER
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
    if request.method == "POST":
        FullName = request.POST["name"]
        EmailAddress = request.POST["email"]
        Subject = request.POST["subject"]
        Phone = request.POST["phone"]
        Message = request.POST["message"]
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            Subject,
            f"You have a message from {FullName} (contacts : {EmailAddress} | {Phone})\n\n {Message}",
            EMAIL_HOST_USER,
            [admin_email],
            fail_silently=False,
        )
        messages.success(
            request, "Your message has been sent. Thank you for you intrest!"
        )
    return render(request, "pages/contact.html", data)
