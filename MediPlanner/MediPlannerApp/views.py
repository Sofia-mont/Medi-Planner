from django.shortcuts import render,redirect
from .models import Enfermera, Paciente, Medicina, Medicamento, Novedades
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

#whatsapp messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def message(self):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')

    return HttpResponse('Hora de medicar al paciente')


# Create your views here.
def login(request):
    return render(request, "MediPlannerApp/index-login.html")

def index(request):
    return render(request, "MediPlannerApp/index.html")

class medicinas(ListView):
    model = Medicina
    template_name ="MediPlannerApp/CRUDMedicinas/medicinas.html"

class añadirMedicina(SuccessMessageMixin, CreateView):
    model = Medicina
    form = Medicina
    template_name ="MediPlannerApp/CRUDMedicinas/añadirMedicina.html"
    fields = "__all__"
    success_message= 'Medicina creada correctamente.'

    def get_success_url(self):
        return reverse('medicinas')

class editarMedicina(SuccessMessageMixin, UpdateView):  
    model = Medicina
    form = Medicina
    template_name ="MediPlannerApp/CRUDMedicinas/editarMedicina.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('medicinas')

class eliminarMedicina(SuccessMessageMixin, DeleteView):
    model = Medicina
    form = Medicina
    fields = "__all__"

    def get_success_url(self):
        success_message= 'Medicina eliminada correctamente.'
        messages.success (self.request, (success_message))
        return reverse('medicinas')

class pacientes(ListView):
    model = Paciente
    template_name ="MediPlannerApp/CRUDPacientes/pacientes.html"

class paciente_info(DetailView):
    model = Paciente
    template_name ="MediPlannerApp/CRUDPacientes/paciente_info.html"

    def get_context_data(self, *args, **kwargs):
        paciente= Paciente.objects.all()
        context = super(paciente_info, self).get_context_data(*args, **kwargs)
        context['medicamentos'] = Medicamento.objects.filter(cedula=self.object).order_by("hora")
        context['novedades'] = Novedades.objects.filter(paciente=self.object)
        return context

class añadirPaciente(SuccessMessageMixin, CreateView):
    model = Paciente
    form = Paciente
    template_name ="MediPlannerApp/CRUDPacientes/añadirPaciente.html"
    fields = "__all__"
    success_message= 'Paciente creado correctamente.'

    def get_success_url(self):
        return reverse('pacientes')

class editarPaciente(SuccessMessageMixin, UpdateView):  
    model = Paciente
    form = Paciente
    template_name ="MediPlannerApp/CRUDPacientes/editarPaciente.html"
    fields = "__all__"
    
    def get_success_url(self):  
        return reverse('pacientes')

class eliminarPaciente(SuccessMessageMixin, DeleteView):
    model = Paciente
    form = Paciente
    fields = "__all__"

    def get_success_url(self):
        success_message= 'Paciente eliminado correctamente.'
        messages.success (self.request, (success_message))
        return reverse('pacientes')

class enfermeras(ListView):
   model = Enfermera
   template_name = "MediPlannerApp/CRUDEnfermeras/enfermeras.html"

class añadirEnfermera(SuccessMessageMixin, CreateView):
    model = Enfermera
    form = Enfermera
    template_name = "MediPlannerApp/CRUDEnfermeras/añadirEnfermera.html"
    fields = "__all__"
    success_message= 'Enfermera/o creado correctamente.'

    def get_success_url(self):
        return reverse('enfermeras')

class editarEnfermera(SuccessMessageMixin, UpdateView):  
    model = Enfermera
    form = Enfermera
    template_name = "MediPlannerApp/CRUDEnfermeras/añadirEnfermera.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('enfermeras')

class eliminarEnfermera(SuccessMessageMixin, DeleteView):
    model = Enfermera
    form = Enfermera
    fields = "__all__"

    def get_success_url(self):
        success_message= 'Enfermera/o eliminado correctamente.'
        messages.success (self.request, (success_message))
        return reverse('enfermeras')

class añadirMedicacion(SuccessMessageMixin, CreateView):
    model = Medicamento
    form = Medicamento
    template_name = "MediPlannerApp/CRUDPacientes/añadirMedicamento.html"
    fields = "__all__"
    success_message= 'Medicamento añadido correctamente.'

    def get_success_url(self):
        return reverse('pacientes')

class editarMedicacion(SuccessMessageMixin, UpdateView):
    model = Medicamento
    form = Medicamento
    template_name = "MediPlannerApp/CRUDPacientes/editarMedicamento.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('pacientes')

class eliminarMedicacion(SuccessMessageMixin, DeleteView):
    model = Medicamento
    form = Medicamento
    fields = "__all__"

    def get_success_url(self):
        success_message= 'Medicamento eliminado correctamente.'
        messages.success (self.request, (success_message))
        return reverse('pacientes')

class añadirNovedad(SuccessMessageMixin, CreateView):
    model = Novedades
    form = Novedades
    template_name = "MediPlannerApp/CRUDPacientes/añadirNovedad.html"
    fields = "__all__"
    success_message= 'Medicamento añadido correctamente.'

    def get_success_url(self):
        return reverse('pacientes')

class editarNovedad(SuccessMessageMixin, UpdateView):
    model = Novedades
    form = Novedades
    template_name = "MediPlannerApp/CRUDPacientes/editarNovedad.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('pacientes')

class eliminarNovedad(SuccessMessageMixin, DeleteView):
    model = Novedades
    form = Novedades
    fields = "__all__"

    def get_success_url(self):
        success_message= 'Novedad eliminado correctamente.'
        messages.success (self.request, (success_message))
        return reverse('pacientes')