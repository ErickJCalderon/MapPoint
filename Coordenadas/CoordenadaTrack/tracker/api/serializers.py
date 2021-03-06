"""Establecemos los modelos a Serializar"""
from django.contrib.auth.models import User

from rest_framework import serializers
from tracker.models import Direccion, Usuario

"""Serializamos el modelo de Usarios estandar"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


"""Serializamos el modelo de Direcciones que hemos creado"""


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id', 'nombre', 'longitud', 'latitud', 'usuario']


"""Serializamos el modelo de Direcciones que hemos creado"""


class Usuarioserializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'dni', 'nombre', 'apellido', 'user', 'email']
