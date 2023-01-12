from django import forms

class ShirtsForm(forms.Form):
    maker = forms.CharField(max_length=100)
    season = forms.IntegerField()