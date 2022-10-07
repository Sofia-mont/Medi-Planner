from django.contrib import admin
from .models import JefeEnfermeras, Enfermera, Turno, Paciente, Medicamento

# Register your models here.

admin.site.register(Enfermera)
admin.site.register(JefeEnfermeras)
admin.site.register(Turno)
admin.site.register(Paciente)
admin.site.register(Medicamento)