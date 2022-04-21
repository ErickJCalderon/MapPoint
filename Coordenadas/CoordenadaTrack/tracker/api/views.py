from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .serializers import DireccionSerializer
from ..models import Direccion

class DireccionApiView(ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticated]
