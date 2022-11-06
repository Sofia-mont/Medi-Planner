from xml.dom.minidom import Document
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index,name="index"),
    path('pacientes/', views.pacientes,name="pacientes"),
    path('pacientes/detalle/<int:pk>', views.paciente_info.as_view(), name="paciente_info"),
    path('añadirPaciente/', views.añadirPaciente, name="añadirPaciente"),
    path('editarPaciente/<int:cedula>', views.editarPaciente, name="editarPaciente"),
    path('eliminarPaciente/<int:cedula>', views.eliminarPaciente, name="eliminarPaciente"),
    path('medicinas/', views.medicinas, name="medicinas"),
    path('añadirMedicina/', views.añadirMedicina, name="añadirMedicina"),
    path('editarMedicina/<int:id>', views.editarMedicina, name="editarMedicina"),
    path('eliminarMedicina/<int:id>', views.eliminarMedicina, name="eliminarMedicina"),
    path('enfermeras/', views.enfermeras, name="enfermeras"),
    path('añadirEnfermera/', views.añadirEnfermera, name="añadirEnfermera"),
    path('editarEnfermera/<int:cedula>', views.editarEnfermera, name="editarEnfermera"),
    path('eliminarEnfermera/<int:cedula>', views.eliminarEnfermera, name="eliminarEnfermera"),
]
