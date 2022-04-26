from django.forms import models

"""Definimos una funcion para comprobar que el usuario existe"""

def usuario_existe(dni, usuario):

    user = models.Usuario.objetcs.filter(dni=dni)
    dir = {}
    while True:
        try:
            if dni:
                user.objects.filter(nombre=usuario)
                if usuario:
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
                    print("El nombre no coincide")
            else:
                print("No no exite ningun usuario con ese DNI")
        except Exception as err:
            print(err)
            print("La consulta que quieres hacer no es posible, introduce otros parametros")

    return dir

nuevo_usuario= {
    'dni': "45678123P" ,
    'nombre': "Rebeca",
    'apellido': "Chambers",
    'user': "zener",
    'email': "rebeca.chambers@meloinvento.com",
}


def crear_usuario(dni=nuevo_usuario['dni'], nombre=nuevo_usuario['nombre']):

    usuario = models.Usuario.objetcs.create(
        dni=dni,
        nombre=nombre,
        apellido=nuevo_usuario['apellido'],
        user= nuevo_usuario['user'],
        email= nuevo_usuario['email']
    )

    return usuario



