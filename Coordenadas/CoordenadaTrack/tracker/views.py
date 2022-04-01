from django.shortcuts import render
from django.views.generic import ListView
from .models import Direccion
from django.http import JsonResponse
from . import models

class DireccionListView(ListView):
    model = Direccion

    def get(self,request):
        contexto = {
            'direcciones': list(Direccion.objects.all())
        }
        return render(request,"direcciones.html",context=contexto)


def direccionesDiccionario(direccion):
    """
    A utility function to convert object of type Blog to a Python Dictionary
    """
    output = {}
    output["title"] = direccion.title
    output["description"] = direccion.description
    output["showcaseImage"] = direccion.showcaseImage.url
    output["dateTimeOfCreation"] = direccion.dateTimeOfCreation.strftime("%m/%d/%Y, %H:%M:%S")
    output["shareURL"] = direccion.shareURL
    output["likes"] = direccion.likes
    output["disLikes"] = direccion.disLikes
    output["bookmarks"] = direccion.bookmarks

    return output

# Function based view
def myView(request):
    # Single Blog
    direccion = models.Direccion.objects.get(id = 1)

    # Multiple Blogs
    direcciones = models.Direccion.objects.all()
    tempDir = []

    # Converting `QuerySet` to a Python Dictionary
    direccion = direccionesDiccionario(direccion)

    for i in range(len(direcciones)):
        tempDir.append(direccionesDiccionario(direcciones[i])) # Converting `QuerySet` to a Python Dictionary

    direcciones = tempDir

    data = {
        "direccion": direccion,
        "direcciones": direcciones
    }

    return JsonResponse(data)