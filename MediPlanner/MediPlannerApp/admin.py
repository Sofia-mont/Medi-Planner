from django.contrib import admin
from .models import JefeEnfermeras, Enfermera, Turno, Paciente, Medicina, Medicamento, Novedades

# Register your models here.

admin.site.register(Enfermera)
admin.site.register(JefeEnfermeras)
admin.site.register(Turno)
admin.site.register(Paciente)
admin.site.register(Medicina)
admin.site.register(Medicamento)
admin.site.register(Novedades)