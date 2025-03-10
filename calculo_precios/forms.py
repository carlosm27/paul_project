from django import forms
from django.forms import ModelForm

from .models import *

class CarneForm(forms.ModelForm):
    nombre = models.CharField(max_length=100)
    peso = models.FloatField(max_length=20)
    precio = models.FloatField(max_length=20)

    class Meta:
        model = Carne
        field = '__all__'