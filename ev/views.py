from django.shortcuts import render, redirect
from ev.form import EventForm, ParticipentForm, CategoryForm
from django.contrib import messages
from ev.models import Event
# Create your views here.


def home(request):
    d = Event.objects.select_related("category").all()[:6]

    for event in d:
        print(event.description)
    return render(request, "banner.html", {"d": d})


def AddEvent(request):
    # Initialize the form instances
    e = EventForm()
    p = ParticipentForm()
    c = CategoryForm()

    if request.method == "POST":
        e = EventForm(request.POST)
        p = ParticipentForm(request.POST)
        c = CategoryForm(request.POST)

        if c.is_valid() and e.is_valid() and p.is_valid():
            # Save the category first
            category = c.save()

            # Save the event and assign the category to it
            event = e.save(commit=False)
            event.category = category  # Attach the created category to the event
            event.save()

            # Save the participant
            participant = p.save(commit=False)
            participant.save()  # Save the participant to get an ID

            # Set the events for the participant (ManyToMany relationship)
            # Use p.cleaned_data['events']
            participant.events.set(p.cleaned_data['events'])

            messages.success(request, "Event Created Successfully")
            return redirect('add_event')

    return render(request, "create_event.html", {"e": e, "p": p, "c": c})


def Event_detail(request, xoxo):
    try:
        event = Event.objects.get(id=xoxo)
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('home')

    return render(request, "event_details.html", {"event": event})


def Update_event(request, id):
    evt = Event.objects.get(id=id)
    e = EventForm(instance=evt)
    p = ParticipentForm(instance = evt)
    if Event.category:
        c = CategoryForm(instance = evt.category)
    else:
        c = CategoryForm()
    if request.method == "POST":
        if Event.category:
            c = CategoryForm(instance = evt.category)
        else:
            c = CategoryForm()
        e = EventForm(request.POST, instance=evt)
        p = ParticipentForm(request.POST)
        
        if c.is_valid() and e.is_valid() and p.is_valid():
            categori = c.save()

            event = e.save(commit=False)
            event.category = categori
            event.save()

            participent = p.save(commit=False)
            participent.save()
            participent.events.set(p.cleaned_data['events'])
            messages.success(request, "Event Updated Successfully")

            redirect('update_event', id=id)

    return render(request, "update.html", {'e': e, 'p': p, 'c': c})
