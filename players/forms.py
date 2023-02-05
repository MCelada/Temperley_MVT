from django import forms
from players.models import Players

# class PlayersForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     age = forms.IntegerField()
#     height = forms.FloatField()
#     position = forms.CharField(max_length=50)
#     image = forms.ImageField()
    
class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ('first_name','last_name','age','height','position','image',)

# def __init__(self, *args, **kwargs):
#     super(PlayersForm, self).__init__(*args, **kwargs)
#     self.fields['image'].required = False