from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('enfermeras/', views.enfermeras,name="indexEnfermeras"),
    path('enfermerasJefe/', views.enfermerasJefe,name="indexEnfermeraJefe"),
]
