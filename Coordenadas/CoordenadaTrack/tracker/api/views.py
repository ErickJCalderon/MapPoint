from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import DireccionSerializer, UserSerializer
from ..models import Direccion

"""Creamos la clase que implementa el modelo de Direcciones"""


class DireccionApiView(ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
