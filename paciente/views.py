from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from paciente.models import Paciente
from .forms import PacienteForm

# Create your views here.

def dashboard(request):
    paciente = Paciente.objects.all()
    return render(request, "paciente/dashboard.html",{"pacientes":paciente})

def create(request):
    form=PacienteForm()
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():

             p = Paciente(
                 nombre=form.cleaned_data['nombre'],
                 apellido=form.cleaned_data['apellido'],
                 edad=form.cleaned_data['edad'],
                 fechaNacimiento=form.cleaned_data['fechaNacimiento'],
                 estatura=form.cleaned_data['estatura'],
                 genero=form.cleaned_data['genero'],
                 peso=form.cleaned_data['peso'],
                 phone=form.cleaned_data['telefono'],
                 direccion=form.cleaned_data['direccion'],
                 documentoIdentidad=form.cleaned_data['documentoIdentidad'],
                 email=form.cleaned_data['email']
             )
             p.save()
             return HttpResponseRedirect(reverse("paciente"))
             
    else:
        return render(request,"paciente/create.html",{"form":form})