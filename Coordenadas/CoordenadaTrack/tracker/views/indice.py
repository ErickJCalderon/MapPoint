from ..utilities.direcciones_utils import *
from django.http import JsonResponse

"""Funcion que devuelve un JSon con los datos obtenidos del metodo listasr_puntos """


def jsonView(request):
    datos = listar_puntos()
    return JsonResponse(datos)
