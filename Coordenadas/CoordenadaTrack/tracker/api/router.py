from rest_framework.routers import DefaultRouter
from .views import DireccionApiView

"""Asignamos a la variable router el default importado"""
router = DefaultRouter()

"""Registramos el router asignando el prefijo a utilizar para refernos al mismo, el nombre y la clase que implementa de la view"""
router.register(prefix='direccion', basename='direccion', viewset=DireccionApiView)
