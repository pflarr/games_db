from django import forms
from games_app.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
