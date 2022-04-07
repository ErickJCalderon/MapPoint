from django.forms import models


def listar_puntos():
    # Multiple Direcciones
    direcciones = models.Direccion.objects.all()
    tempDir = []

    for i in direcciones:
        i.pk
        tempDir.append(
            {
            'id': i.id,
            'nombre': i.nombre,
            'latitud': i.latitud,
            'longitud': i.longitud
             }
        )

    return tempDir
