from django.urls import path
from .views import inicio, login, registro, cerrar, publicar, publicaciones, perfil, detalle, eliminar_comentario, eliminar_publicacion, cerrar_trato, cancelar_trato, editar_perfil, eliminar_cuenta, calificar_usuario, eliminar_calificacion, usuarios_perfil, notificaciones, eliminar_notificacion, eliminar_todas_notificaciones, sobre_nosotros

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
    path('cerrar_trato/<int:publicacion_id>/<int:comentario_id>/', cerrar_trato, name='cerrar_trato'),
    path('cancelar_trato/<int:publicacion_id>/', cancelar_trato, name='cancelar_trato'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('eliminar_cuenta/', eliminar_cuenta, name='eliminar_cuenta'),
    path('calificar_usuario/<int:publicacion_id>/', calificar_usuario, name='calificar_usuario'),
    path('eliminar_calificacion/<int:publicacion_id>/', eliminar_calificacion, name='eliminar_calificacion'),
    path('usuario/<str:username>/', usuarios_perfil, name='usuarios_perfil'),
    path('notificaciones/', notificaciones, name='notificaciones'),
    path('notificaciones/eliminar/<int:id>/', eliminar_notificacion, name='eliminar_notificacion'),
    path('notificaciones/eliminar_todas/', eliminar_todas_notificaciones, name='eliminar_todas_notificaciones'),
    path('sobre_nosotros', sobre_nosotros, name='sobre_nosotros'),
]