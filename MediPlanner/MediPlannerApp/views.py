from django.shortcuts import render
# from Enfermeras.models import Enfermeras PARA CUANDO SE CREE LA BASE DE DATOS
# Create your views here.

def enfermeras(request):
    # PARA CUANDO SE CREE LA BASE DE DATOS enfermeras = Enfermeras.objects.all()
    return render(request, "Enfermeras/index-nurse.html")


def enfermerasJefe(request):
    return render(request, "EnfermerasJefe/index-chief-nursing.html")
