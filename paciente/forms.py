from django import forms
from paciente.models import Paciente,Turnos,HistorialMedico
from users.models import User
from GestiOpti import settings 


class PacienteForm(forms.ModelForm):
    fechaNacimiento=forms.DateField(label='Fecha de Nacimiento', input_formats=settings.DATE_INPUT_FORMATS,widget= forms.DateInput(attrs={'class':'datepicker','type':'Date'}))
    class Meta:
          model = Paciente
          fields =  "__all__"
  
class TurnosForm(forms.ModelForm):
    class Meta:
          model = Turnos
          widgets = {
            'fecha': forms.DateInput(attrs={'class':'datepicker','type':'Date'}),
            'hora': forms.DateInput(attrs={'class':'timepicker','type':'Time'}),
          }
          labels = {
            "id_usuario":"Profesional Medico"
          }
          fields = '__all__'

class HistorialMedicoForm(forms.ModelForm):
      motivo = forms.CharField(widget=forms.Textarea)
      observaciones = forms.CharField(widget=forms.Textarea)
      class Meta:
          model = HistorialMedico
          fields = ('motivo','observaciones')
          