from django.shortcuts import render
# from Enfermeras.models import Enfermeras PARA CUANDO SE CREE LA BASE DE DATOS
# Create your views here.

def enfermeras(request):
    # PARA CUANDO SE CREE LA BASE DE DATOS enfermeras = Enfermeras.objects.all()
    return render(request, "index-nurse.html")


def enfermerasJefe(request):
    return render(request, "index-chief-nursing.html")

def pacientes(request):
    return render(request, "pacientes.html")

def medicinas(request):
    return render(request, "pacientes.html")

def enfermeras(request):
    return render(request, "pacientes.html")
