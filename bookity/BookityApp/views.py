from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import PublicacionForm

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
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return render(request, 'BookityApp/inicio.html')
        else:
            return render(request, 'BookityApp/login.html', {'form': form})
    return render(request, 'BookityApp/login.html', {'form': AuthenticationForm()})

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