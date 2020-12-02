from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from paciente.models import Paciente,Turnos
from .forms import PacienteForm,TurnosForm
from users.models import User

# Create your views here.

def dashboard(request):
    paciente = Paciente.objects.all()
    return render(request, "paciente/dashboard.html",{"pacientes":paciente})

def create(request):
    form=PacienteForm()
    contexto = {
        'form':form
    }
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse("paciente"))
             
    else:
        return render(request,"paciente/create.html",contexto)

def turnos(request):
    turnos = Turnos.objects.all()
    return render(request, "turnos/dashboard.html",{"turnos":turnos})

def turnos_create(request):
    form=TurnosForm()
    form.fields['id_usuario'].queryset = User.objects.filter(rol=2)
    if request.method == 'POST':
        form = TurnosForm(request.POST)
        if form.is_valid():

             t = Turnos(
                 id_paciente=form.cleaned_data['id_paciente'],
                 id_usuario=form.cleaned_data['id_usuario'],
                 fecha=form.cleaned_data['fecha'],
                 hora=form.cleaned_data['hora'],
                 asistencia=form.cleaned_data['asistencia']
             )
             t.save()
             return HttpResponseRedirect(reverse("turnos"))
             
    else:
        return render(request,"turnos/create.html",{"form":form})

def turnos_edit(request,id):
    turnos = Turnos.objects.get(id = id)
    if request.method == 'GET':
        form = TurnosForm(instance = turnos)
        form.fields['id_usuario'].queryset = User.objects.filter(rol=2)
        contexto = {
            'form':form
        }
        return render(request,"turnos/create.html",contexto)
    else:
        form = TurnosForm(request.POST,instance=turnos)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("turnos"))
def turnos_delete(request,id):
    turnos = Turnos.objects.get(id = id)
    turnos.delete()
    return HttpResponseRedirect(reverse("turnos"))

