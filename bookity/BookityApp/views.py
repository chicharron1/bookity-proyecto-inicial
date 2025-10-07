from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

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