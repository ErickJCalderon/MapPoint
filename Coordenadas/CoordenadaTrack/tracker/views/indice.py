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
                datos['ok'] = lista['ok']
        except:
            datos['error'] = "Se ha producido un error en la respuesta del servidor"
        return JsonResponse(datos)

"""Request para el registro de una direccion"""
id_direccion = 1
nombre_usuario = "Erick"


def direccion(request):
    if request.method == 'POST':
        datos = {}
        try:
            direccion = registrar_direccion(id_direccion, nombre_usuario)
            if 'error' in direccion:
                datos['error'] = direccion['error']
            else:
                datos['ok'] = direccion['ok']
        except:
            datos['error'] = "Se ha producido un error en la respuesta del servidor"
        return datos


"""Request para la creacion de un usuario"""


def usuario(request):
    if request.method == 'POST':
        usuario = crear_usuario()
        messages.success("El usuario se registro exitosamente")
        return JsonResponse(usuario)
    else:
        messages.error("No ha sido posible crearlo")






