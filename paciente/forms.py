from django import forms


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

