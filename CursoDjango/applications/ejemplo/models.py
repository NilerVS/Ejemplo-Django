from django.db import models

# Create your models here.


#la bade de datos tendra nombres, apellidopaterno  y apellido materno

class Usuario(models.Model):

    nombre = models.CharField('nombre', max_length=50)
    apellidoPaterno = models.CharField('apellidop', max_length=100)
    apellidoMaterno = models.CharField('apellidom', max_length=100)
   
    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellidoPaterno

 