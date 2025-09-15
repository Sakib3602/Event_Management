from django.shortcuts import render
from ev.form import EventForm, Participent, CategoryForm

# Create your views here.
def home(request):
    return render(request, "banner.html")

def AddEvent(request):
    e = EventForm()
    p = Participent()
    c = CategoryForm()

    if request.method == "POST":
        e = EventForm(request.POST)
        p = Participent(request.POST)
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
            participant.save()

            # Set the events for the participant (ManyToMany relationship)
            participant.events.set(e.cleaned_data['events'])

            # Optionally, you can redirect or display a success message
            return render(request, "success.html", {"message": "Event and participant added successfully"})

    return render(request, "create_event.html", {"e": e, "p": p, "c": c})
