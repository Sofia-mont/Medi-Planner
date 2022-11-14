from xml.dom.minidom import Document
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index,name="index"),
    path('pacientes/', views.pacientes.as_view(), name="pacientes"),
    path('pacientes/detalle/<int:pk>', views.paciente_info.as_view(), name="paciente_info"),
    path('pacientes/añadirPaciente/', views.añadirPaciente.as_view(), name="añadirPaciente"),
    path('pacientes/editarPaciente/<int:pk>', views.editarPaciente.as_view(), name="editarPaciente"),
    path('pacientes/eliminarPaciente/<int:pk>', views.eliminarPaciente.as_view(), name="eliminarPaciente"),
    path('pacientes/añadirMedicacion/', views.añadirMedicacion.as_view(), name="añadirMedicacion"),
    path('pacientes/detalle/editarMedicacion/<int:pk>', views.editarMedicacion.as_view(), name="editarMedicacion"),
    path('pacientes/detalle/eliminarMedicacion/<int:pk>', views.eliminarMedicacion.as_view(), name="eliminarMedicacion"),
    path('pacientes/añadirNovedad/', views.añadirNovedad.as_view(), name="añadirNovedad"),
    path('pacientes/detalle/editarNovedad/<int:pk>', views.editarNovedad.as_view(), name="editarNovedad"),
    path('pacientes/detalle/eliminarNovedad/<int:pk>', views.eliminarNovedad.as_view(), name="eliminarNovedad"),
    path('medicinas/', views.medicinas.as_view(), name="medicinas"),
    path('medicinas/añadirMedicina/', views.añadirMedicina.as_view(), name="añadirMedicina"),
    path('medicinas/editarMedicina/<int:pk>', views.editarMedicina.as_view(), name="editarMedicina"),
    path('medicinas/eliminarMedicina/<int:pk>', views.eliminarMedicina.as_view(), name="eliminarMedicina"),
    path('enfermeras/', views.enfermeras.as_view(), name="enfermeras"),
    path('enfermeras/añadirEnfermera/', views.añadirEnfermera.as_view(), name="añadirEnfermera"),
    path('enfermeras/editarEnfermera/<int:pk>', views.editarEnfermera.as_view(), name="editarEnfermera"),
    path('enfermeras/eliminarEnfermera/<int:pk>', views.eliminarEnfermera.as_view(), name="eliminarEnfermera"),

    path('message', views.message),

]
