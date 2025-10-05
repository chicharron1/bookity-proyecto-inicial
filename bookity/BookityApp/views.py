from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Aquí puedes agregar lógica adicional, como iniciar sesión al usuario
            return render(request, 'BookityApp/registro.html', {'form': UserCreationForm()})
    else:
        form = UserCreationForm()
    return render(request, 'BookityApp/registro.html', {'form': form})

def inicio(request):
    return render(request, 'BookityApp/inicio.html')

def login(request):
    return render(request, 'BookityApp/login.html')