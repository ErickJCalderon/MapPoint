from django.forms import models


def listar_puntos():
    # Multiple Direcciones
    direcciones = models.Direccion.objects.all()
    tempDir = []

    try:
        id_exists = direcciones.id
        if id_exists != 0:
            print("Consultando direcciones")
    except direcciones.DoesNotExist:
        print("No existen valores")

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
