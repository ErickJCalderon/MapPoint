from django.forms import models

"""Definimos una funcion que nos lista los puntos de las coordenadas"""


def listar_puntos():
    """asignamos todos los objetos de la tabla Direccion, a una lista llamada direcciones"""
    direcciones = models.Direccion.objects.all()

    """creamos un diccionario temporal para las direccionmes que vamos guardando en la lista """
    tempDir = []

    """Comprobamos mediante un try/except que las direcciones recibidas no estan vacias preguntando
    si el campo de id es un numero distinto de 0 (es decir que existe por lo menos un registro)"""
    try:
        id_exists = direcciones.id
        if id_exists != 0:
            print("Consultando direcciones")
    except direcciones.DoesNotExist:
        print("No existen valores")

    """For para rellenar el diccionario (tempDir) con los campos asociados de los objetos recibidos"""
    for i in direcciones:
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

    return tempDir


def registrar_direccion(identifier, nombre):

    while True:
        try:
            direccion = models.Direccion.objects.filter(id=identifier)
            if direccion:
                comprobar = models.Direccion.objects.filter(nombre=nombre)
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

        except Exception as err:
            print(err)
            print()

    return resgistro
