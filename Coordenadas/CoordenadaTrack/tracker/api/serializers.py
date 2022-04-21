from django.contrib.auth.models import User
from rest_framework import serializers

from tracker.models import Direccion


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['id', 'nombre', 'longitud' , 'latitud']

