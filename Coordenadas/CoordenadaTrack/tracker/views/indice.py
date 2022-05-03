from ..utilities.direcciones_utils import *
from django.http import JsonResponse
from django.shortcuts import render
from ..utilities.usuario_utils import *
from django.contrib import messages

"""Funcion que devuelve un JSon con los datos obtenidos del metodo listasr_puntos """


def jsonView(request):
    if request.method == 'GET':
        datos = listar_puntos()
        return JsonResponse(datos)



"""Request para la creacion de un usuario"""


def usuario(request):
    if request.method == 'POST':
        usuario = crear_usuario()
        messages.success("El usuario se registro exitosamente")
        return JsonResponse(usuario)
    else:
        messages.error("No ha sido posible crearlo")


id = 1
nombre = "Casa Erick"
"""Request para la creacion de una direccion"""


def direccion(request):
    if request.method == 'POST':
        direccion = registrar_direccion(id, nombre)
        messages.success("Se ha registrado exitosamente")
        return JsonResponse(direccion)
    else:
        messages.error("No ha sido posible registrar la direccion")
