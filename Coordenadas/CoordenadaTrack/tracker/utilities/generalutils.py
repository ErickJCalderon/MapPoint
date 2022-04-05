from django.forms import models

def json_diccionario():
    # Multiple Direcciones
    direcciones = models.Direccion.objects.all()
    tempDir = []

    for i in direcciones:
        i.pk
        tempDir.append(
            {'latitud': i.latitud},
            {'longitud': i.longitud},
        )

    return tempDir