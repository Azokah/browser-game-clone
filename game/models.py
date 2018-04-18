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
    civilizacion = models.OneToOneField(Civilizacion, on_delete=models.CASCADE)
    def __str__(self):
        return self.user

class Aldea(models.Model):
    nombre = models.CharField(max_length=50)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, default=None)
    x = models.IntegerField()
    y = models.IntegerField()
    poblation = models.IntegerField()
    def __str__(self):
        return self.nombre + "-" + self.jugador.user.username

class Mensaje(models.Model):
    titulo = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=250)
    emisor = models.ForeignKey(Jugador, related_name='emisor', on_delete=models.CASCADE)
    receptor = models.ForeignKey(Jugador, related_name='receptor', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo

