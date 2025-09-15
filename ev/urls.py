
from django.urls import path 
from ev.views import home, AddEvent
urlpatterns = [
    path("", home),
    path("add_event/", AddEvent , name = "add_event")
]