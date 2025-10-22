from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import PublicacionForm
from .models import Publicacion

def registro(request):
    mensaje_error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'BookityApp/registro.html', {'form': UserCreationForm(), 'mensaje_error': ''})
        else:
            mensaje_error = "Inválido :("
    else:
        form = UserCreationForm()
    return render(request, 'BookityApp/registro.html', {'form': form, 'mensaje_error': mensaje_error})

def inicio(request):
    return render(request, 'BookityApp/inicio.html')

def login(request):
    form = AuthenticationForm(data=request.POST or None)

    form.fields['username'].widget.attrs.update({
        'class': 'input-login',
        'placeholder': 'Ingresa tu usuario'
    })
    form.fields['password'].widget.attrs.update({
        'class': 'input-login',
        'placeholder': 'Ingresa tu contraseña'
    })

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return render(request, 'BookityApp/inicio.html')
    
    return render(request, 'BookityApp/login.html', {'form': form})



def cerrar(request):
    logout(request)
    return redirect('inicio')

def publicar(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.user = request.user
            publicacion.save()
            return redirect('inicio')
        else:
            return render(request, 'BookityApp/publicar.html', {'form': form})
    else:
        form = PublicacionForm()
    return render(request, 'BookityApp/publicar.html', {'form': form})

def publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')
    return render(request, 'BookityApp/publicaciones.html', {
        'publicaciones': publicaciones
    })