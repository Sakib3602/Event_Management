from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "banner.html")



def AddEvent(request):
    return render(request, "add_event.html")