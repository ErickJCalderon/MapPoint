from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import DireccionSerializer, UserSerializer, Usuarioserializer
from ..models import Direccion, Usuario

"""Creamos la clase que implementa el modelo de Direcciones"""


class DireccionApiView(ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]


"""Creamos la clase que implementa el modelo UserDefault de Django"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


"""Creamos la clase que implementa el modelo Usuario"""


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializer
    permission_classes = [permissions.IsAuthenticated]
