from utilities.generalutils import *
from django.http import JsonResponse


def jsonView(self, request):
    datos = json_diccionario()
    return JsonResponse(datos)
