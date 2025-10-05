from django.urls import path
from .views import inicio, login, registro

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]