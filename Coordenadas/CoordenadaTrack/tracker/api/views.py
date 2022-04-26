from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import DireccionSerializer
from ..models import Direccion

"""Creamos la clase que implementa el modelo de Direcciones"""
class DireccionApiView(ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]