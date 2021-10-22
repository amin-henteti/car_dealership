from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cars.views import data
from contacts.models import Contact


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
            messages.error(request, " Password does not match.\nTry again ")
            return redirect("register")
        else:
            if User.objects.filter(username=Username).exists():
                messages.error(
                    request,
                    " Username already exist.\nPlease try another one or sign in ",
                )
                return redirect("register")
            elif User.objects.filter(email=EmailAddress).exists():
                messages.error(request, " Email already exist.\nTry to sign in ")
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
                messages.success(request, "You're now logged in. Welcome!")
                return redirect("dashboard")
                messages.success(
                    request, "Successfully registred in our site.. Thank you!"
                )
                return redirect("login")
    return render(request, "account/register.html", data)


def login(request):
    if request.method == "POST":
        Password = request.POST["password"]
        Username = request.POST.get("username")
        print(f"{Password} is password, {Username} is username")
        if Username.find("@") > -1:
            EmailAdress = Username
            user = auth.authenticate(email=EmailAdress, password=Password)
        else:
            user = auth.authenticate(username=Username, password=Password)
        if user is None:
            messages.error(request, " Invalid login credentials ")
            print(" Invalid login credentials ")
            return redirect("login")
        else:
            auth.login(request, user)
            print("You're now logged in. Welcome!")
            messages.success(request, "You're now logged in. Welcome!")
            return redirect("dashboard")

    return render(request, "account/login.html", data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        # messages.success(request, "You are successfully logged out. See you soon")
        print("You are successfully logged out. See you soon")
        return redirect("home")
    return redirect("home")


# if not registred/logged in then redirect to log in page
@login_required
def dashboard(request):
    inquiries = Contact.objects.order_by("-created_date").filter(
        user_id=request.user.id
    )
    data2 = {"inquiries": inquiries}
    return render(request, "account/dashboard.html", {**data, **data2})
