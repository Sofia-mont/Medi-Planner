from django.shortcuts import render
from .models import Enfermera, Paciente, Medicamento
# Create your views here.

def index(request):
    return render(request, "MediPlannerApp/index.html")

def pacientes(request):
    pacientes= Paciente.objects.all()
    return render(request, "MediPlannerApp/pacientes.html",{'pacientes':pacientes})

def medicinas(request):
    medicinas= Medicamento.objects.all()
    return render(request, "MediPlannerApp/medicinas.html",{'medicinas':medicinas})

def enfermeras(request):
    enfermeras = Enfermera.objects.all()
    return render(request, "MediPlannerApp/enfermeras.html",{'enfermeras':enfermeras})
