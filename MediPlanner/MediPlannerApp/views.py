from django.shortcuts import render,redirect
from .models import Enfermera, Paciente, Medicamento, JefeEnfermeras, Turno
from .forms import EnfermeraForm
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

def añadirEnfermera(request):
    form = EnfermeraForm()

    if request.method == 'POST':
        form = EnfermeraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enfermeras')

    context = {
        'form': form,
    }
    return render(request, 'MediPlannerApp/añadirEnfermera.html', context)

def editarEnfermera(request, cedula):  
    enfermera = Enfermera.objects.get(cedula=cedula)
    form = EnfermeraForm(instance=enfermera)

    if request.method == 'POST':
        form = EnfermeraForm(request.POST, instance=enfermera)
        if form.is_valid():
            form.save()
            return redirect('enfermeras')

    context = {
        'enfermera': enfermera,
        'form': form,
    }
    return render(request, 'MediPlannerApp/editarEnfermera.html', context)

def eliminarEnfermera(request, cedula):
    enfermera = Enfermera.objects.get(cedula=cedula)

    if request.method == 'POST':
        enfermera.delete()
        return redirect('enfermeras')

    context = {
        'enfermera': enfermera,
    }
    return render(request, 'MediPlannerApp/eliminarEnfermera.html', context)