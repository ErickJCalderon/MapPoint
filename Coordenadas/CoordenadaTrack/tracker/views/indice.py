from ..utilities.direcciones_utils import *
from django.http import JsonResponse
from django.shortcuts import render
from ..utilities.usuario_utils import *
from django.contrib import messages

"""Funcion que devuelve un JSon con los datos obtenidos del metodo listasr_puntos """


def jsonView(request):
    if request.method == 'GET':
        datos = {}

        """Hemos creado un diccionario datos y asignamos la funcion listar_puntos a lista para saber el estado 
        que devuelve"""
        try:
            lista = listar_puntos()
            """En caso de error, asignamos al diccionario dicho error para poder retornarlo mas adelante,
             en caso de acierto se devuele la lista de todo lo que contenga en formato JsonResponse"""
            if 'error' in lista:
                datos['error'] = lista['error']
            else:
                datos['ok'] = lista['ok']
        except:
            datos['error'] = "Se ha producido un error en la respuesta del servidor"
        return JsonResponse(datos)


"""Variables para una prueba"""
id_direccion = 1
nombre_usuario = "Erick"

"""Request para el registro de una direccion"""


def direccion(request):
    if request.method == 'POST':
        datos = {}
        """Hemos creado un diccionario datos y asignamos la funcion registrar_direcco con las variables de prueba
           a direccion para saber el estado que devuelve"""
        try:
            direccion = registrar_direccion(id_direccion, nombre_usuario)
            """En caso de error, asignamos al diccionario dicho error para poder retornarlo mas adelante,
            en caso de acierto se devuele la lista de todo lo que contenga en formato JsonResponse"""
            if 'error' in direccion:
                datos['error'] = direccion['error']
            else:
                datos['ok'] = direccion['ok']
        except:
            datos['error'] = "Se ha producido un error en la respuesta del servidor"
        return datos


"""Request para la creacion de un usuario"""


