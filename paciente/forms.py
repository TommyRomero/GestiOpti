from django import forms
from paciente.models import Paciente,Turnos,HistorialMedico
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

class HistorialMedicoForm(forms.ModelForm):
      motivo = forms.CharField(widget=forms.Textarea)
      observaciones = forms.CharField(widget=forms.Textarea)
      class Meta:
          model = HistorialMedico
          fields = ('motivo','observaciones')
          