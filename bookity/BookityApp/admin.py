from django.contrib import admin
from .models import Publicacion, Comentario, Perfil
# Register your models here.

admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Perfil)