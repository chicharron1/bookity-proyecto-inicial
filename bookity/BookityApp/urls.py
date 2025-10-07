from django.urls import path
from .views import inicio, login, registro, cerrar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('cerrar_sesion/', cerrar, name='cerrar'),
]