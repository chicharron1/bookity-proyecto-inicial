from django.urls import path
from .views import inicio, login, registro, cerrar, publicar, publicaciones, perfil

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', cerrar, name='cerrar'),
    path('publicar/', publicar, name='publicar'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('perfil/', perfil, name='perfil'),
]