from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .models import User



# Home
def Home(request):
    context = {}
    return render(request, "home.html", context)


# Sing Up
def SingUp(request):
    if request.method == 'POST':

        try:
            User.objects.create_user(
                username=request.POST['username'],
                email = request.POST["email"],
                user_type = request.POST["user_type"],
                password = request.POST["password"],
            )

            messages.success(request, "Your account successfully created!")

            return redirect("singin")
        except:
            messages.warning(request, "username and email must be unique!")


    context = {}
    return render(request, "sing_up.html", context)


# Sing In
def SingIn(request):
    if request.method == "POST":
        user = authenticate(
            email = request.POST["email"],
            password = request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "user not found")

    context = {}
    return render(request, "sing_in.html", context)


# Logout
def Logout(request):
    logout(request)
    return redirect("/")
