from django import forms
from paciente.models import Paciente
from users.models import User


class PacienteForm(forms.Form):
    GENERO_TYPE_CHOICES = (
        ('F',"FEMENINO"),
        ('M',"MASCULINO")
    )
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField()
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateField()
    email = forms.EmailField()
    genero = forms.ChoiceField(choices=GENERO_TYPE_CHOICES)
    telefono =forms.CharField()
    direccion=forms.CharField(max_length=300)
    documentoIdentidad=forms.CharField()
    estatura=forms.DecimalField(max_digits=6,decimal_places=2)
    peso=forms.DecimalField(max_digits=6,decimal_places=2)

class TurnosForm(forms.Form):
    ASISTENCIA_CHOICES = (
        (1,"Si"),
        (2,"No")
    )
    id_paciente=forms.ModelChoiceField(queryset=Paciente.objects.all(),empty_label="Selecciona un paciente",label="Paciente") 
    id_usuario=forms.ModelChoiceField(queryset=User.objects.filter(rol=2),empty_label="Selecciona médico",label="Médico") 
    fecha=forms.DateField()
    hora=forms.TimeField()
    asistencia=forms.TypedChoiceField(choices=ASISTENCIA_CHOICES,coerce = str)


