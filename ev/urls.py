
from django.urls import path 
from ev.views import home, AddEvent, Event_detail, Update_event
urlpatterns = [
    path("", home, name="home"),
    path("add_event/", AddEvent , name = "add_event"),
    path("event/<int:xoxo>/", Event_detail , name="event_detail"),
    path("update/<int:id>/", Update_event, name="update_event"),
]