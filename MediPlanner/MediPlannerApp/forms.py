from django import forms
from django.forms import ModelForm
from .models import Enfermera, Paciente

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

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ('cedula','nombres', 'apellidos', 'sexo', 'habitacion', 'fecha_salida', 'novedades', 'enfermeras')

        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cedula'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexo'}),
            'habitacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Habitacion'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'FechaSalida'}),
            'novedades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Novedades'}),
            'enfermeras': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Enfermeras'}),
        }