from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion, Perfil, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'descripcion', 'contacto', 'tipo', 'ubicacion', 'latitud', 'longitud']
        widgets = {
            'latitud': forms.HiddenInput(),
            'longitud': forms.HiddenInput(),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['latitud_defecto', 'longitud_defecto']
        widgets = {
            'latitud_defecto': forms.HiddenInput(),
            'longitud_defecto': forms.HiddenInput(),
        }
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['latitud_defecto', 'longitud_defecto']
        widgets = {
            'latitud_defecto': forms.HiddenInput(),
            'longitud_defecto': forms.HiddenInput(),
        }

class CalificacionForm(forms.Form):
    calificacion = forms.IntegerField(min_value=1, max_value=5, label='Calificación (1-5)')