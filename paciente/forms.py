from django import forms
from paciente.models import Paciente,Turnos
from users.models import User


class PacienteForm(forms.ModelForm):
    class Meta:
          model = Paciente
          fields =  "__all__"
  
class TurnosForm(forms.ModelForm):
    class Meta:
          model = Turnos
          widgets = {
            'fecha': forms.DateInput(attrs={'class':'datepicker'}),
          }
          fields = '__all__'
          