from django.db import models

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

# Create your models here.
