from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

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
    radio_marcador = models.FloatField(default=50)
    estado = models.CharField(max_length=20, choices=[('Disponible', 'Disponible'), ('Cerrado', 'Cerrado')], default='Disponible')
    trato_cerrado_con = models.ForeignKey('auth.User', related_name='trato_cerrado_con', on_delete=models.SET_NULL, null=True, blank=True)
    calificacion = models.IntegerField(null=True, blank=True)
    resena = models.TextField(null=True, blank=True)

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
    radio_marcador_defecto = models.FloatField(default=50)
    puntaje_usuario = models.IntegerField(default=0)
    nivel_usuario = models.CharField(max_length=20, choices=[('Nuevo', 'Nuevo'), ('Medio', 'Medio'), ('KPro', 'KPro')], default='Nuevo')
    promedio_calificaciones = models.FloatField(default=0.0, null=True, blank=True)
    usuarios_seguidos = models.ManyToManyField('self', blank=True)

    def seguir_usuario(self, usuario):
        self.usuarios_seguidos.add(usuario)
        self.save()
    
    def dejar_de_seguir_usuario(self, usuario):
        self.usuarios_seguidos.remove(usuario)
        self.save()

    def actualizar_promedio_calificaciones(self):
        from .models import Publicacion  # evita import circular
        promedio = (
            Publicacion.objects.filter(user=self.user, calificacion__isnull=False)
            .aggregate(Avg('calificacion'))['calificacion__avg']
        )
        self.promedio_calificaciones = promedio or 0
        self.save()
    
    def actualizar_nivel(self):
        if self.puntaje_usuario >= 100:
            self.nivel_usuario = 'KPro'
        elif self.puntaje_usuario >= 50:
            self.nivel_usuario = 'Medio'
        else:
            self.nivel_usuario = 'Nuevo'
        self.save()