
from django.urls import path 
from ev.views import home
urlpatterns = [
    path("", home)
    
]