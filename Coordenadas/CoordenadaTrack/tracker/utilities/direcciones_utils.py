from django.forms import models

"""Definimos una funcion que nos lista los puntos de las coordenadas"""


def listar_puntos():
    tempDir = []
    data = {}
    obj_direcciones = models.Direccion.objects.all()
    try:
        if obj_direcciones:
            for i in obj_direcciones:
                i.pk
                tempDir.append(
                    {
                        'id': i.id,
                        'nombre': i.nombre,
                        'latitud': i.latitud,
                        'longitud': i.longitud,
                        'usuario': i.usuario,
                    }
                )
            data['ok'] = tempDir
        else:
            data['error'] = " No se ha podido obtener datos de las direcciones"
    except:
        data['error'] = " Se ha producido un error al obtener datos del usuario"
    return data


"""Metodo para registrar una direccion"""


def registrar_direccion(identifier_direccion, nombre_usuario):
    data = {}

    try:
        comprobar_usuario = models.Usuario.objects.filter(nombre=nombre_usuario)
        """Comprobamos si el usuario existe"""

        if comprobar_usuario:
            comprobar_direccion = models.Direccion.objects.filter(id=identifier_direccion)
            """En caso de existir, comprobamos  la direccion, si existe rellenamos el resto de campos para
            completar el registro"""
            if comprobar_direccion:
                models.Direccion.objects.create(
                    nombre=comprobar_direccion.nombre,
                    latitud=comprobar_direccion.latitud,
                    longitud=comprobar_direccion.longitud,
                    usuario=nombre_usuario,
                )
                data['OK'] = "Direccion registrada con exito"
            else:
                print("La direccion no existe, crear nueva direccion")
                print("Nombre de la direccion: ")
                nombre_direccion: input()
                print("Latitud: ")
                latitud = input()
                print("Longitud: ")
                longitud = input()

                models.Direccion.objects.create(
                    nombre=nombre_direccion,
                    latitud=latitud,
                    longitud=longitud,
                    usuario=nombre_usuario,
                )
                data['OK'] = "Direccion creada con exito"
        else:
            data['error'] = "El usuario no existe"
    except:
        data['error'] = "Parametros introducidos erroneos"

    return data
