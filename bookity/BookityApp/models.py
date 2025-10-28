from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Publicacion(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=[('Intercambio', 'Intercambio'), ('Donación', 'Donación')], default='Donación')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_comentario']

class Perfil(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    latitud_defecto = models.FloatField(null=True, blank=True)
    longitud_defecto = models.FloatField(null=True, blank=True)
    nivel_usuario = models.IntegerField(default=0)