from django.db import models
from django.contrib.auth.models import User

"""Creaciond del modelo Usuarios"""
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    """Asignacion de FK al auth_user"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.nombre


"""Creacion del modelo Direccion"""
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    longitud = models.DecimalField(max_digits=12, decimal_places=6)
    latitud = models.DecimalField(max_digits=12, decimal_places=6)

    """Asignacion de FK al modelo Usuario"""
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Coordenadas"
        verbose_name_plural = "Coordenadass"

    def __str__(self):
        return self.nombre
