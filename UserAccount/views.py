from django.shortcuts import render, redirect


# Home
def Home(request):
    context = {}
    return render(request, "home.html", context)


# Sing Up
def SingUp(request):
    context = {}
    return render(request, "sing_up.html", context)


# Sing In
def SingIn(request):
    context = {}
    return render(request, "sing_in.html", context)


# Logout
def Logout(request):
    return redirect("/")
