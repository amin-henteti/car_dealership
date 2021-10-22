from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from carwebsite.settings import EMAIL_HOST_USER
from contacts.models import Contact
from django.core.mail import send_mail

# Create your views here.


def inquiry(request):
    if request.method == "POST":
        UserID = int(request.POST["user_id"])
        FirstName = request.POST["firstname"]
        LastName = request.POST["lastname"]
        Topic = request.POST["customer_need"]
        EmailAddress = request.POST["email"]
        Phone = request.POST["phone"]
        Addresss = request.POST["address"]

        Car_title = request.POST["car_title"]
        Car_id = int(request.POST["car_id"])
        Car_price = int(request.POST["car_price"])

        Message = request.POST["message"]
        has_contacted = Contact.objects.all().filter(user_id=UserID, car_id=Car_id)
        if UserID != 0 and has_contacted:
            messages.error(
                request,
                "Thank you for your interest in this car. You already sent us a message. We will back to you shortly",
            )
            return redirect("/cars/" + str(Car_id))

        contact = Contact.objects.create(
            user_id=UserID,
            first_name=FirstName,
            last_name=LastName,
            address=Addresss,
            email=EmailAddress,
            phone=Phone,
            customer_need=Topic,
            car_title=Car_title,
            car_id=Car_id,
            car_price=Car_price,
            message=Message,
        )
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            Topic,
            f"{Message}\nYou have an inquiry for the car {Car_title}.\n Login in the admin side for more informations.",
            EMAIL_HOST_USER,
            [admin_email],
            fail_silently=False,
        )
        contact.save()
        if User.is_authenticated:
            messages.success(
                request,
                "Thank you for your interest in this car. The message was sent. We will back to you in a few",
            )
            return redirect("dashboard")

        else:
            messages.success(
                request,
                "Thank you for your interest in this car. The message was sent from unregisterd account. Please consider signing up.",
            )
            return redirect("/cars/" + str(Car_id))

    return render(request)
