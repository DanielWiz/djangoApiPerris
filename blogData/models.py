from django.db import models

# Create your models here.
class MisPerros(models.Model):
    Nombre = models.CharField(max_length=100)
    Detalles = models.CharField(max_length=500)
    Foto = models.ImageField()
    DISPONIBILIDAD = [
    ('D', 'Disponible'),
    ('N', 'No Disponible')
    ]
    Disponibilidad = models.CharField(max_length=1,choices=DISPONIBILIDAD)