from django.db import models


class Direccion(models.Model):
    CALLE = 'c/'
    AVENIDA = 'avd'
    PLAZA = 'plza'

    VIA_CHOISES=[
        (CALLE, 'Calle'),
        (AVENIDA, 'Avenida'),
        (PLAZA, 'Plaza'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    longitud = models.DecimalField(max_digits=12, decimal_places=6)
    latitud = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        verbose_name = "Coordenadas"
        verbose_name_plural = "Coordenadass"

    def __str__(self):
        return self.id
