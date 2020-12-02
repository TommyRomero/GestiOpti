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
      #Mostar campo requerido al crear user en consola 
      REQUIRED_FIELDS = ['rol','email']



