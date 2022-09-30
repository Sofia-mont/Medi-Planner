from django.apps import AppConfig


class MediplannerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MediPlannerApp'

class EnfermerasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Enfermeras'

class PacientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pacientes'

class EnfermerasjefeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EnfermerasJefe'

class MedicinasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Medicinas'
