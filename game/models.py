from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Index(models.Model):
    def __str__(self):
        return "index"

class Civilizacion(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    user = models.CharField(max_length=50, unique=True)
    civilizacion = models.ForeignKey(Civilizacion, on_delete=models.CASCADE,related_name='jugadores')
    def __str__(self):
        return self.user

class Mensaje(models.Model):
    titulo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=250)
    emisor = models.ForeignKey(Jugador, related_name='emisor', on_delete=models.CASCADE)
    receptor = models.ForeignKey(Jugador, related_name='receptor', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

class Mapa(models.Model):
    name = models.CharField(max_length=50, default="Patagonia")
    width = models.IntegerField(default=20)
    height = models.IntegerField(default=20)
    mapSize = models.IntegerField(default=2000)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): ##Solo puede haber un objeto mapa
        if Mapa.objects.exists() and not self.pk:
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Mapa instance')
        return super(Mapa, self).save(*args, **kwargs)
    
class Celda(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    size = models.IntegerField(default=100)
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE, related_name='celdas')


class Aldea(models.Model):
    nombre = models.CharField(max_length=50)
    poblation = models.IntegerField(default=10)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, default=None)
    posicion = models.OneToOneField(Celda, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.nombre