from django.db import models

class Planta(models.Model):
    nombre_comun = models.CharField(max_length=200)
    nombre_cientifico = models.CharField(max_length=200, blank=True, null=True)
    fecha_adquisicion = models.DateField()
    imagen = models.ImageField(upload_to='planta/', blank=True, null=True)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_comun
