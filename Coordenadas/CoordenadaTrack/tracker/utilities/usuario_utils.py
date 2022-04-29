from django.forms import models

"""Definimos una funcion para comprobar que el usuario existe"""


def usuario_existe(identifier, dni):
    user = models.Usuario.objetcs.filter(id=identifier)
    dir = {}
    while True:

        try:
            """Comprobamos si el usuario existe mediante el id """
            if identifier:
                user.objects.filter(dni=dni)
                """En caso de existir comprobamos mediante el dni, si el usuario existe, guardamos sus datos en un 
                diccionario"""
                if dni:
                    print("El Usuario exite")
                    for i in user:
                        i.pk
                        dir.append(
                            {
                                'id': i.id,
                                'dni': i.dni,
                                'nombre': i.nombre,
                                'apellido': i.apellido,
                                'user': i.user,
                                'email': i.email,
                            }
                        )
                    break
                else:
                    print("El dni no coincide")
            else:
                print("No existe ningun usuario con ese ID")
        except Exception as err:
            print(err)
            print("La consulta que quieres hacer no es posible, introduce otros parametros")

    return dir


nuevo_usuario = {
    'dni': "45678123P",
    'nombre': "Rebeca",
    'apellido': "Chambers",
    'user': "zener",
    'email': "rebeca.chambers@meloinvento.com",
}

"""Metodo para crear un usuario, para esto hemos predefinido un usuario, retorna el usuario"""


def crear_usuario(dni=nuevo_usuario['dni'], nombre=nuevo_usuario['nombre']):
    """"""
    usuario = models.Usuario.objetcs.create(
        dni=dni,
        nombre=nombre,
        apellido=nuevo_usuario['apellido'],
        user=nuevo_usuario['user'],
        email=nuevo_usuario['email']
    )

    return usuario
