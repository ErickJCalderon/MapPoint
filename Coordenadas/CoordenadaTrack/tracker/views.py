from django.shortcuts import render
from django.views.generic import ListView
from .models import Direccion
from django.http import JsonResponse
from . import models


class DireccionListView(ListView):
    model = Direccion

    def get(self, request):
        contexto = {
            'direcciones': list(Direccion.objects.all())
        }
        return render(request, "direcciones.html", context=contexto)


def direccionesDiccionario(direccion):
    """
    A utility function to convert object of type Blog to a Python Dictionary
    """

    data = {}
    data["id"] = direccion.id
    data["nombre"] = direccion.nombre
    data["longitud"] = direccion.longitud
    data["latitud"] = direccion.latitud

    return data


def myView(request):
    # Single Direccion
    direccion = models.Direccion.objects.get(id=1)

    # Multiple Direcciones
    direcciones = models.Direccion.objects.all()
    tempDir = []

    # Converting `QuerySet` to a Python Dictionary
    direccion = direccionesDiccionario(direccion)

    for i in range(len(direcciones)):
        tempDir.append(direccionesDiccionario(direcciones[i]))  # Converting `QuerySet` to a Python Dictionary

    direcciones = tempDir

    data = {
        "direccion": direccion,
        "direcciones": direcciones
    }

    return JsonResponse(data)
