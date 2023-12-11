from django.db import models
import json
from .planta import Planta


class Pregunta(models.Model):
    TIPO_OPCIONES = 'opciones'
    TIPO_NUMERICA = 'numerica'
    TIPO_CHOICES = [
        (TIPO_OPCIONES, 'Opciones'),
        (TIPO_NUMERICA, 'Numérica'),
    ]

    texto = models.CharField(max_length=200)
    opciones = models.TextField(blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default=TIPO_OPCIONES)

    def get_opciones(self):
        if self.tipo == self.TIPO_OPCIONES:
            return json.loads(self.opciones)
        return None

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


class PreguntaCuidado(models.Model):
    registro_cuidado = models.ForeignKey(RegistroCuidado, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    orden = models.IntegerField()

    def __str__(self):
        return f"Pregunta '{self.pregunta.texto}' en {self.registro_cuidado}"

class SesionCuidado(models.Model):
    registro_cuidado = models.ForeignKey(RegistroCuidado, on_delete=models.CASCADE)
    usuario = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sesión para {self.registro_cuidado} por {self.usuario.username} comenzó en {self.fecha_inicio}"

class RespuestaCuidado(models.Model):
    sesion_cuidado = models.ForeignKey(SesionCuidado, on_delete=models.CASCADE)
    pregunta_cuidado = models.ForeignKey(PreguntaCuidado, on_delete=models.CASCADE, null=True)
    respuesta = models.CharField(max_length=200, null=True)  # Almacena la opción seleccionada
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Respuesta '{self.respuesta}' para '{self.pregunta.texto}' en {self.registro_cuidado}"
