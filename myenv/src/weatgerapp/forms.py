from django import forms
from . models import *
class FormCity(forms.ModelForm):
    class Meta:
        model=City
        fields=['name']
        widgets={'name':forms.TextInput(attrs={'placeholder':'Enter your city or another location...'})}
