from django import forms
from GestionPedido.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
          model = Pedido
          widgets = {
            'id_usuario': forms.HiddenInput(attrs={'readonly':'true'})
          }
          fields = '__all__'