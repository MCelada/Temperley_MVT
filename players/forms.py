from django import forms
from players.models import Players
    
class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ('first_name','last_name','age','height','position','image',)

