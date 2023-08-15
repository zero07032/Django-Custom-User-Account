from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("singup", views.SingUp, name="singup"),
    path("singin", views.SingIn, name="singin"),
    path("logout", views.Logout, name="logout"),
]
