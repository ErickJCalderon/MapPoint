from rest_framework import routers
from .views import DireccionApiView, UserViewSet, UsuarioViewSet

"""Asignamos a la variable router el default importado"""
router = routers.DefaultRouter()

"""Registramos el router asignando el prefijo a utilizar para referirnos al mismo,
 el nombre y la clase que implementa de la view"""
router.register(prefix='usuario', basename='usuario', viewset=UsuarioViewSet)
router.register(prefix='direccion', basename='direccion', viewset=DireccionApiView)
router.register(r'users', viewset=UserViewSet)
