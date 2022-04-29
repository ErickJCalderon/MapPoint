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
            data['error'] = " No se ha `podido obtener datos de las direcciones"
    except:
        data['error'] = " Se ha producido un error al obtener datos del usuario"
    return data


"""Metodo para registrar una direccion"""


def registrar_direccion(identifier_direccion, nombre_usuario):
    while True:
        """Comprobamos si el id existe, en caso de error salta una exception"""
        try:
            direccion = models.Direccion.objects.filter(id=identifier_direccion)

            """En caso de existir, comprobamos si esta asignada a un nombre de usuario"""
            if direccion:
                comprobar = models.Usuario.objects.filter(nombre=nombre_usuario)
                """Una vez comprobado decimos al usuario que ya existe dicha direccion registrada y paramos el bucle
                En caso contrario, decimos al usuario que registre la nueva direccion para el usuario"""
                if comprobar:
                    print("Esta direccion existe en la base de datos")
                    break
                else:
                    print("Introduce las demas variables")
                    print("Latitud: ")
                    latitud = input()
                    print("Longitud: ")
                    longitud = input()
                    print("Usuario: ")
                    usuario = input()
                    resgistro = models.Direccion.objects.create(
                        id=identifier,
                        nombre=nombre,
                        latitud=latitud,
                        longitud=longitud,
                        usuario=usuario,
                    )
                    break

        except Exception as err:
            print(err)
            print("No se ha podido registrar nada")

    return resgistro
