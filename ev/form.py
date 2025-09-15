from django import forms
from ev.models import Event, Participent, Category
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "date", "time", "location", "category"]
        widgets = {
            "date" : forms.DateField(widget=forms.SelectDateWidget()),
            "time" : forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'})) 
        }
class Participent(forms.ModelForm):
    class Meta:
        model = Participent
        fields = ["name", "email", "events"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
