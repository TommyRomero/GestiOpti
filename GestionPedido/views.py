from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from GestionPedido.models import Pedido
from .forms import PedidoForm
from users.models import User
# Create your views here.
def dashboard(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedido/dashboard.html",{"pedidos":pedidos})

def create(request):
    data = {"id_usuario":7,"id_paciente":1}
    form=PedidoForm(initial=data)
    form.fields['id_usuario'].queryset = User.objects.filter(rol=3)
    contexto = {
        'form':form
    }
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse("pedido"))
             
    else:
        return render(request,"paciente/create.html",contexto)