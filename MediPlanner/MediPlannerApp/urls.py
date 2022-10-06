from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index,name="index"),
    path('pacientes/', views.pacientes,name="pacientes"),
    path('medicinas/', views.medicinas,name="medicinas"),
    path('enfermeras/', views.enfermeras, name="enfermeras"),
]
