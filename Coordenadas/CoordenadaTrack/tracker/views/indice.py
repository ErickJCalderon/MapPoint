from ..utilities.direcciones_utils import *
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from ..utilities.usuario_utils import *
from django.contrib import messages

"""Funcion que devuelve un JSon con los datos obtenidos del metodo listasr_puntos """


def jsonView(request):
    if request.method == 'GET':
        datos = {}

        try:
            lista = listar_puntos()
            if 'error' in lista:
                datos['error']= lista['error']
            else:
                datos['Ok'] = lista['Ok']
        except:
            datos['error'] = "Se ha producido un error en la respuesta del servidor"
        return JsonResponse(datos)

"""Request para el registro de una direccion"""

def direccion(request):
    if request.method == 'POST':
        direccion = registrar_direccion(id, nombre)
        messages.success("Se ha registrado exitosamente")
        return JsonResponse(direccion)
    else:
        messages.error("No ha sido posible registrar la direccion")


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



