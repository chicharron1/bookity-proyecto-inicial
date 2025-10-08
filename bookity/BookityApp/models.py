from django.db import models

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=[('Venta', 'Venta'), ('Intercambio', 'Intercambio'), ('Donación', 'Donación')], default='Donación')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
