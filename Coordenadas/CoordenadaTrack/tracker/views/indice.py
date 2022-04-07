from ..utilities.generalutils import *
from django.http import JsonResponse


def jsonView(request):
    datos = listar_puntos()
    return JsonResponse(datos)
