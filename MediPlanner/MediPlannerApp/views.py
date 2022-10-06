from django.shortcuts import render
# from Enfermeras.models import Enfermeras PARA CUANDO SE CREE LA BASE DE DATOS
# Create your views here.

def index(request):
    # PARA CUANDO SE CREE LA BASE DE DATOS enfermeras = Enfermeras.objects.all()
    return render(request, "MediPlannerApp/index.html")

def pacientes(request):
    return render(request, "MediPlannerApp/pacientes.html")

def medicinas(request):
    return render(request, "MediPlannerApp/medicinas.html")

def enfermeras(request):
    return render(request, "MediPlannerApp/enfermeras.html")
