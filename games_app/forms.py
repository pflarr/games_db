from django import forms
from django.forms.formsets import formset_factory
from django.contrib.admin import widgets
from games_app.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event

class GameReqForm(forms.Form):
    game = forms.CharField()
    comment = forms.CharField(required=False)
    bringing = forms.BooleanField(required=False)

GameReqFormset = formset_factory(GameReqForm, extra=9)



