from django import forms
from ev.models import Event, Participent, Category

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        
        # Optionally, you can add widgets to style the form inputs (e.g., with Tailwind CSS)
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class ParticipentForm(forms.ModelForm):
    class Meta:
        model = Participent
        fields = ['name', 'email', 'events']
        widgets = {
            'events': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
