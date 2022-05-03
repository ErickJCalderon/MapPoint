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
    """Comprobamos si el la direccion existe, en caso de error salta una exception"""
    try:
        direccion = models.Direccion.objects.filter(id=identifier_direccion)
        """En caso de existir, comprobamos si el usuario existe"""
        if direccion:
            comprobar = models.Usuario.objects.filter(nombre=nombre_usuario)
            if comprobar:
                print("Introduce las demas variables")
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
                data['error'] = "No existe el usuario"
        else:
            data['error'] = "La direccion no existe"
    except :
        data['error'] = "Parametros introducidos erroneos"

    return data