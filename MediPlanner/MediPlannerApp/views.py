from django.shortcuts import render,redirect
from .models import Enfermera, Paciente, Medicina, JefeEnfermeras, Medicamento, Novedades
from .forms import EnfermeraForm, PacienteForm, MedicinaForm
from django.views import generic
# Create your views here.
def login(request):
    return render(request, "MediPlannerApp/index-login.html")

def index(request):
    return render(request, "MediPlannerApp/index.html")

def medicinas(request):
   medicinas = Medicina.objects.all()
   return render(request, "MediPlannerApp/medicinas.html",{'medicinas':medicinas})

def añadirMedicina(request):
    form = MedicinaForm()

    if request.method == 'POST':
        form = MedicinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicinas')

    context = {
        'form': form,
    }
    return render(request, 'MediPlannerApp/añadir.html', context)

def editarMedicina(request, id):  
    medicina = Medicina.objects.get(id=id)
    form = MedicinaForm(instance=medicina)

    if request.method == 'POST':
        form = MedicinaForm(request.POST, instance=medicina)
        if form.is_valid():
            form.save()
            return redirect('medicinas')

    context = {
        'medicina': medicina,
        'form': form,
    }
    return render(request, 'MediPlannerApp/editar.html', context)

def eliminarMedicina(request, id):
    medicina = Medicina.objects.get(id=id)

    if request.method == 'POST':
        medicina.delete()
        return redirect('medicinas')

    context = {
        'medicina': medicina,
    }
    return render(request, 'MediPlannerApp/eliminar.html', context)

def pacientes(request):
    pacientes= Paciente.objects.all()
    return render(request, "MediPlannerApp/pacientes.html",{'pacientes':pacientes})

class paciente_info(generic.DetailView):
    model = Paciente
    template_name ="MediPlannerApp/paciente_info.html"

    def get_context_data(self, *args, **kwargs):
        paciente= Paciente.objects.all()
        context = super(paciente_info, self).get_context_data(*args, **kwargs)
        context['medicamentos'] = Medicamento.objects.filter(cedula=self.object)
        context['novedades'] = Novedades.objects.filter(paciente=self.object)
        return context

def añadirPaciente(request):
    form = PacienteForm()

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacientes')

    context = {
        'form': form,
    }
    return render(request, 'MediPlannerApp/añadir.html', context)

def editarPaciente(request, cedula):  
    paciente = Paciente.objects.get(cedula=cedula)
    form = PacienteForm(instance=paciente)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('pacientes')

    context = {
        'paciente': paciente,
        'form': form,
    }
    return render(request, 'MediPlannerApp/editar.html', context)

def eliminarPaciente(request, cedula):
    paciente = Paciente.objects.get(cedula=cedula)

    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')

    context = {
        'paciente': paciente,
    }
    return render(request, 'MediPlannerApp/eliminar.html', context)

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
    return render(request, 'MediPlannerApp/añadir.html', context)

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
    return render(request, 'MediPlannerApp/editar.html', context)

def eliminarEnfermera(request, cedula):
    enfermera = Enfermera.objects.get(cedula=cedula)

    if request.method == 'POST':
        enfermera.delete()
        return redirect('enfermeras')

    context = {
        'enfermera': enfermera,
    }
    return render(request, 'MediPlannerApp/eliminar.html', context)
