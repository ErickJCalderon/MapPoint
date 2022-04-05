from django.forms import models
from django.shortcuts import render

def json_diccionario(request):
    # Multiple Direcciones
    direcciones = models.Direccion.objects.all()
    tempDir = []

    for i in direcciones:
        i.pk
        tempDir.append(
            {'latitud': i.latitud},
            {'longitud': i.longitud},
        )
    return render(request,'direcciones.html',{'tempDir': tempDir})