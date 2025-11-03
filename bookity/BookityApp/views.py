from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .forms import PublicacionForm, PerfilForm, ComentarioForm, CalificacionForm
from .models import Publicacion, Perfil, Comentario
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def registro(request):
    mensaje_error = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            user = form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            return redirect('login')
        else:
            mensaje_error = "Inválido :("
    else:
        form = UserCreationForm()
        perfil_form = PerfilForm()
    return render(request, 'BookityApp/registro.html', {'form': form, 'perfil_form': perfil_form, 'mensaje_error': mensaje_error})

def inicio(request):
    return render(request, 'BookityApp/inicio.html')

def login(request):
    mensaje_error = ''
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
        else:
            mensaje_error = "Usuario o contraseña incorrectos"

    return render(request, 'BookityApp/login.html', {'form': form, 'mensaje_error': mensaje_error})

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
            publicacion.user.perfil.puntaje_usuario += 10
            publicacion.user.perfil.actualizar_nivel()
            publicacion.save()
            return redirect('inicio')
        else:
            return render(request, 'BookityApp/publicar.html', {'form': form})
    else:
        form = PublicacionForm()
    return render(request, 'BookityApp/publicar.html', {'form': form})

def publicaciones(request):
    publicaciones = Publicacion.objects.filter(estado='Disponible').order_by('-fecha_publicacion')
    query = request.GET.get('q')
    tipo_filtro = request.GET.get('tipo_filtro')
    if tipo_filtro == 'Intercambios':
        publicaciones = publicaciones.filter(tipo='Intercambio')
    elif tipo_filtro == 'Donaciones':
        publicaciones = publicaciones.filter(tipo='Donación')
    
    if query:
        publicaciones = publicaciones.filter(
            Q(titulo__icontains=query) | Q(descripcion__icontains=query)
        )
    return render(request, 'BookityApp/publicaciones.html', {
        'publicaciones': publicaciones
    })

def perfil(request):
    publicaciones = Publicacion.objects.filter(user=request.user).order_by('-fecha_publicacion')
    return render(request, 'BookityApp/perfil.html', {
        'publicaciones': publicaciones,'perfil': Perfil.objects.get(user=request.user)
    })

def detalle(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    comentario_form = ComentarioForm()
    calificacion_form = CalificacionForm()

    ya_comento = False
    if request.user.is_authenticated:
        ya_comento = Comentario.objects.filter(publicacion=publicacion, user=request.user).exists()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        calificacion_form = CalificacionForm(request.POST)

        if 'calificacion' in request.POST and calificacion_form.is_valid():
            calificacion = calificacion_form.cleaned_data['calificacion']
            publicacion.calificación = calificacion
            publicacion.save()
            return redirect('detalle', publicacion_id=publicacion.id)

        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.user = request.user
            comentario.publicacion = publicacion
            comentario.user.perfil.puntaje_usuario += 5
            comentario.user.perfil.actualizar_nivel()
            comentario.save()
            return redirect('detalle', publicacion_id=publicacion.id)
    else:
        comentario_form = ComentarioForm()
    return render(request, 'BookityApp/detalle.html', {'publicacion': publicacion, 'comentario_form': comentario_form, 'ya_comento': ya_comento, 'calificacion_form': calificacion_form})


@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id, user=request.user)
    publicacion_id = comentario.publicacion.id
    comentario.user.perfil.puntaje_usuario -= 5
    comentario.user.perfil.save()
    comentario.user.perfil.actualizar_nivel()
    comentario.delete()
    return redirect('detalle', publicacion_id=publicacion_id)

@login_required
def eliminar_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id, user=request.user)
    if request.method == 'POST':
        publicacion.user.perfil.puntaje_usuario -= 10
        publicacion.user.perfil.save()
        publicacion.user.perfil.actualizar_nivel()
        publicacion.delete()
        return redirect('publicaciones')

def cerrar_trato(request, publicacion_id, comentario_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id, user=request.user)
    comentario = get_object_or_404(Comentario, id=comentario_id, publicacion=publicacion)
    if request.method == 'POST':
        publicacion.estado = 'Cerrado'
        publicacion.trato_cerrado_con = comentario.user
        perfil_usuario = Perfil.objects.get(user=request.user)
        perfil_usuario.puntaje_usuario += 20
        perfil_usuario.actualizar_nivel()
        publicacion.save()
        return redirect('detalle', publicacion_id=publicacion.id)

def cancelar_trato(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id, user=request.user)
    if request.method == 'POST':
        publicacion.estado = 'Disponible'
        publicacion.trato_cerrado_con = None
        perfil_usuario = Perfil.objects.get(user=request.user)
        perfil_usuario.puntaje_usuario -= 20
        perfil_usuario.save()
        perfil_usuario.actualizar_nivel()
        publicacion.save()
        return redirect('detalle', publicacion_id=publicacion.id)

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('registro')

@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, user=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'BookityApp/editar_perfil.html', {'form': form})

@login_required
def calificar_usuario(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    autor = publicacion.user
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.cleaned_data['calificacion']
            publicacion.calificacion = calificacion
            if calificacion == 1:
                autor.perfil.puntaje_usuario -= 8
            if calificacion == 2:
                autor.perfil.puntaje_usuario -= 4
            if calificacion == 3:
                autor.perfil.puntaje_usuario += 2
            if calificacion == 4:
                autor.perfil.puntaje_usuario += 6
            if calificacion == 5:
                autor.perfil.puntaje_usuario += 10
            autor.perfil.save()
            autor.perfil.actualizar_nivel()
            publicacion.save()
            return redirect('detalle', publicacion_id=publicacion.id)
    else:
        form = CalificacionForm()
    return render(request, 'BookityApp/calificar_usuario.html', {'form': form, 'publicacion': publicacion})