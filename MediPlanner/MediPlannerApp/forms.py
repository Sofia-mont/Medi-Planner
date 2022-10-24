from django import forms
from django.forms import ModelForm
from .models import Enfermera

class EnfermeraForm(ModelForm):
    class Meta:
        model = Enfermera
        fields = ('cedula','nombres', 'apellidos', 'telefono', 'jefe', 'turno')

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'jefe': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Jefe'}),
            'turno': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Turno'}),
        }