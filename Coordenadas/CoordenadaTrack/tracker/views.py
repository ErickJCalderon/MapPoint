from django.shortcuts import render
from django.views.generic import ListView
from .models import Direccion
from django.http import JsonResponse
from . import models


class DireccionListView(ListView):
    model = Direccion

    """def get(self, request):
        contexto = {
            'direcciones': list(Direccion.objects.all())
        }
        return render(request, "direcciones.html", context=contexto)
"""

    def direccionesDiccionario(direccion):
        output = {
            "id": direccion.id,
            "nombre": direccion.nombre,
            "longitud": direccion.longitud,
            "latitud": direccion.latitud,
        }

        return output


    def jsonView(self, request):
        # Single Direccion
        direccion = models.Direccion.objects.get(id=1)

        # Multiple Direcciones
        direcciones = models.Direccion.objects.all()
        tempDir = []

        # Converting `QuerySet` to a Python Dictionary
        direccion = request.direccionesDiccionario(direccion)

        for i in range(len(direcciones)):
            tempDir.append(request.direccionesDiccionario(direcciones[i]))  # Converting `QuerySet` to a Python Dictionary

        direcciones = tempDir

        data = {
            "direccion": direccion,
            "direcciones": direcciones
        }

        return JsonResponse(data)
