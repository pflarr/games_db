from django import forms
from django.contrib.admin import widgets
from games_app.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            self.fields['when'].widget = widgets.AdminDateWidget()
