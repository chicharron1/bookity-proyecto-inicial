from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion, Perfil

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'descripcion', 'contacto', 'tipo', 'ubicacion', 'latitud', 'longitud']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['latitud_defecto', 'longitud_defecto']
        widgets = {
            'latitud_defecto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa la latitud'
            }),
            'longitud_defecto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa la longitud'
            }),
        }
