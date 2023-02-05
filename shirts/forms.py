from django import forms
from shirts.models import Shirts

# class ShirtsForm(forms.Form):
#     maker = forms.CharField(max_length=100)
#     season = forms.IntegerField()
#     image = forms.ImageField()

class ShirtsForm(forms.ModelForm):
    class Meta:
        model = Shirts
        fields = ('maker','season','image',)