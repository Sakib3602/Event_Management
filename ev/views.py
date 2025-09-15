from django.shortcuts import render , redirect
from ev.form import EventForm, ParticipentForm, CategoryForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "banner.html")


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
            participant.events.set(p.cleaned_data['events'])  # Use p.cleaned_data['events']

            messages.success(request, "Task Created Successfully")
            return redirect('add_event')

    return render(request, "create_event.html", {"e": e, "p": p, "c": c})
