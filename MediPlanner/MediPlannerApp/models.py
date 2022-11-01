from django.db import models
import uuid

class Turno(models.Model):
    ingreso = models.CharField(max_length=50, blank=True)
    salida = models.CharField(max_length=50, blank= True)

    class Meta:
        verbose_name="turno"
        verbose_name_plural="turnos"
    def __str__(self):
        return "Ingreso: " + self.ingreso + " | Salida: " + self.salida

class JefeEnfermeras(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField()

    class Meta:
        verbose_name="Jefe"
        verbose_name_plural="Jefes"
    def __str__(self):
        return self.nombres + " " + self.apellidos

class Enfermera(models.Model):
    cedula = models.TextField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.IntegerField()
    jefe = models.ManyToManyField(JefeEnfermeras)
    turno = models.ManyToManyField(Turno)

    class Meta:
        verbose_name="enfermera"
        verbose_name_plural="enfermeras"

    def __str__(self):
        return self.nombres

class Medicina(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.CharField(max_length=10)
    invima = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    via_administracion = models.CharField(max_length=40)

    class Meta:
        verbose_name="medicina"
        verbose_name_plural="medicinas"
    def __str__(self):
        return self.nombre + " " + self.cantidad

class Medicacion(models.Model):
    medicina = models.ManyToManyField(Medicina)
    hora = models.TimeField()
    dosis = models.CharField(max_length=50)

    class Meta:
        verbose_name="medicacion"
        verbose_name_plural="medicacion"
    def __str__(self):
        return self.medicina + ", " + self.dosis

class Paciente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    habitacion = models.CharField(max_length=10)
    fecha_salida=models.DateTimeField()
    novedades = models.TextField()
    enfermeras = models.ManyToManyField(Enfermera)
    medicina= models.ManyToManyField(Medicina)

    class Meta:
        verbose_name="paciente"
        verbose_name_plural="pacientes"
    def __str__(self):
        return self.nombres + " " + self.apellidos

#solucionar relacionamiento de campos

class Suministro_Medicamento(models.Model):
    Id_suministroMedicamento = models.IntegerField(primary_key=True)
    Id_paciente = models.IntegerField()
    Id_Medicamento = models.IntegerField()
    hora_Medicacion = models.TimeField()
    dosis = models.CharField(max_length=50)

    class Meta:
        verbose_name="Suministro_Medicamento"
        verbose_name_plural="Suministro_Medicamentos"
    def __str__(self):
        return self.hora_Medicacion + ", " + self.dosis

class Dosis_Paciente(models.Model):
    Dosis = models.ForiegnKey(Suministro_Medicamento, on_delete=models.CASCADE)
    Paciente = models.ForiegnKey(Paciente, on_delete=models.CASCADE, related_name="pacientes")
