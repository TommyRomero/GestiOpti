from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
      USER_TYPE_CHOICES = (
      (1, 'Secretaría'),
      (2, 'Profesional Médico'),
      (3, 'Ventas'),
      (4, 'Taller'),
      (5, 'Gerencia'),
  )

      rol = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
      especialidad = models.TextField(max_length=200,default="")
      #Mostar campo requerido al crear user en consola 
      REQUIRED_FIELDS = ['rol','especialidad','first_name','last_name','email']

      def __str__(self):
        if self.rol == 2:
          return self.first_name + " " + self.last_name + " - " + (self.especialidad if self.especialidad!="" else "Sin Especialidad")
        else:
          return self.first_name + " " + self.last_name
          



