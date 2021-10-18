from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from cars.views import data


def register(request):
    """
    register a user in the database.
    """
    if request.method == "POST":
        FirstName = request.POST["firstname"]
        LastName = request.POST["lastname"]
        Username = request.POST["username"]
        EmailAddress = request.POST["email"]
        Password = request.POST["password"]
        ConfirmPassword = request.POST["confirm_password"]
        if Password != ConfirmPassword:
            messages.error(request, " Password does not match ")
            return redirect("register")
        else:
            if User.objects.filter(username=Username).exists():
                messages.error(request, " Username already exist ")
                return redirect("register")
            elif User.objects.filter(email=EmailAddress).exists():
                messages.error(request, " Email already exist ")
                return redirect("register")
            else:  # all tests are passed
                user = User.objects.create(
                    first_name=FirstName,
                    last_name=LastName,
                    username=Username,
                    email=EmailAddress,
                    password=Password,
                )
                auth.login(request, user)
                user.save()
                messages.success(request, "You're now logged In")
                return redirect("dashboard")
                messages.success(request, "Successfully registred. Thank you")
                return redirect("login")
    return render(request, "account/register.html", data)


def login(request):
    if request.method == "POST€":
        Username = request.POST["username"]
        Password = request.POST["password"]
        user = auth.authenticate(username=Username, password=Password)
        if user is None:
            messages.error(request, " Invelid login credentials ")
            return redirect("login")
        else:
            auth.login(request, user)
            messages.success(request, " welcome back ")
            return redirect("dashboard")

    return render(request, "account/login.html", data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are successfully logged out")
        return redirect("home")
    return redirect("home")


def dashboard(request):
    return render(request, "account/dashboard.html", data)
