from django.urls import path
from user.views import Sign_Up
urlpatterns = [
    path("signup/", Sign_Up, name="signup")

]
