from django.db import models
from users.models import User

# Create your models here.
class Paciente(models.Model):
    GENERO_TYPE_CHOICES = (
        ('F',"FEMENINO"),
        ('M',"MASCULINO")
    )
    nombre =models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    edad=models.IntegerField(blank=False)
    fechaNacimiento=models.DateField()
    genero=models.CharField(max_length=2,choices=GENERO_TYPE_CHOICES)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    direccion=models.CharField(max_length=300)
    documentoIdentidad=models.CharField("documento de identidad",max_length=10,unique=True)
    estatura=models.DecimalField(max_digits=6,decimal_places=2)
    peso=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Turnos(models.Model):
    ASISTENCIA_CHOICES = (
        (1,"SI"),
        (2,"NO")
    )
    id_paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    fecha=models.DateField()
    hora=models.TimeField()
    asistencia=models.PositiveSmallIntegerField(choices=ASISTENCIA_CHOICES)

