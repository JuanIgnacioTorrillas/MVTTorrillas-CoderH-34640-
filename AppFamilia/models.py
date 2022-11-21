from django.db import models
from datetime import date,datetime

#ACA VAN LAS CLASES DEL MODELO


class familiar (models.Model):
    
    nombre=models.CharField(max_length=80) #STR
    
    fecha_de_nacimiento=models.DateTimeField() #Fecha
    
    dni=models.IntegerField() #Numero
    
    def __str__(self):
        return self.nombre+" "+self.fecha_de_nacimiento+" "+self.dni
    
