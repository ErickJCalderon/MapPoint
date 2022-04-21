from rest_framework.routers import DefaultRouter

from .views import DireccionApiView

router = DefaultRouter()

router.register(prefix='direccion', basename='direccion', viewset=DireccionApiView)
