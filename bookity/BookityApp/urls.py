from django.urls import path
from .views import inicio, login, registro, cerrar, publicar, publicaciones, perfil, detalle, eliminar_comentario, eliminar_publicacion

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', cerrar, name='cerrar'),
    path('publicar/', publicar, name='publicar'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('perfil/', perfil, name='perfil'),
    path('publicacion/<int:publicacion_id>/', detalle, name='detalle'),
    path('comentario/eliminar/<int:comentario_id>/', eliminar_comentario, name='eliminar_comentario'),
    path('eliminar_publicacion/<int:publicacion_id>/', eliminar_publicacion, name='eliminar_publicacion'),
]