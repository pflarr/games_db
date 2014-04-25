from django import forms
from django.contrib import admin
from games_app.models import Event, Game

admin.site.register(Event)
admin.site.register(Game)

class MultiEmailField(forms.EmailField):
    

class UserCreationForm(forms.Form):
    
    emails = forms.CharField(widget=forms.Textarea)
    is_admin = forms.BooleanField(required=False)

