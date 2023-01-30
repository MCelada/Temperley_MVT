from django import forms
from players.models import Players

class PlayersForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    height = forms.FloatField()
    position = forms.CharField(max_length=50)
    
