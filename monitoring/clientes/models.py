from django.db import models
from solicitudes.models import Solicitud

class Cliente(models.Model):
    
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
   

    def __str__(self):
      return '%s %s' % (self.nombre, self.telefono)

