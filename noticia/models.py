from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# models.py
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Reportero(User, models.Model):
    #nombre = models.CharField(max_length=80)
    #apellidos = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10, blank=True)
    #email = models.EmailField()
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(default='1900-01-01')
    foto = models.ImageField(upload_to='fotos/', blank=True)
    acta_nacimiento = models.FileField(upload_to='actas/', blank=True)

    def getEdad(self):
        """Calcula la edad a partir de la fecha de nacimiento."""
        hoy = date.today()  # Obtiene la fecha actual
        edad = hoy.year - self.fecha_nacimiento.year  # Calcula la diferencia de años

        # Ajusta la edad si el cumpleaños no ha ocurrido este año
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1

        return edad