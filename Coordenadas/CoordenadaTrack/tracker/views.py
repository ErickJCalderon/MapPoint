from utilities.generalutils import *
from django.http import JsonResponse


def jsonView():
    datos = json_diccionario()
    return JsonResponse(datos)
