from django.db import models
import json
from .planta import Planta


class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    opciones = models.TextField()

    def get_opciones(self):
        return json.loads(self.opciones)

    def __str__(self):
        return self.texto


class RegistroCuidado(models.Model):
    ESTADOS = [
        ('ABIERTO', 'Abierto'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADO', 'Completado'),
    ]

    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    usuario = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=12, choices=ESTADOS, default='ABIERTO')

    def __str__(self):
        return f"{self.estado} - Cuidado de {self.planta.nombre_comun} por {self.usuario.username}"



class RespuestaCuidado(models.Model):
    registro_cuidado = models.ForeignKey(RegistroCuidado, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200)  # Almacena la opción seleccionada
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE)
    orden = models.IntegerField()

    def __str__(self):
        return f"Respuesta '{self.respuesta}' para '{self.pregunta.texto}' en {self.registro_cuidado}"
