from django import forms
from ev.models import Event, Participent, Category


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "date", "time", "location", "category"]
        widgets = {
            "date": forms.SelectDateWidget(),  # Dropdown for date
            "time": forms.TimeInput(attrs={'type': 'time'}),  # Time input for time
        }

# Create Participant Form
class ParticipentForm(forms.ModelForm):
    class Meta:
        model = Participent
        fields = ["name", "email", "events"]

# Create Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
