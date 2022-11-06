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

class Paciente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    habitacion = models.CharField(max_length=10)
    fecha_salida=models.DateTimeField()
    enfermeras = models.ManyToManyField(Enfermera)

    class Meta:
        verbose_name="paciente"
        verbose_name_plural="pacientes"
    def __str__(self):
        return str(self.cedula)

class Medicamento(models.Model):
    cedula = models.ManyToManyField(Paciente)
    medicamento = models.ManyToManyField(Medicina)
    hora = models.TimeField()
    dosis = models.CharField(max_length=50)

    class Meta:
        verbose_name="Medicamento"
        verbose_name_plural="Medicamentos"
    def __str__(self):
        return self.dosis

class Novedades(models.Model):
    paciente= models.ManyToManyField(Paciente)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    class Meta:
        verbose_name="novedad"
        verbose_name_plural="novedades"
    def __str__(self):
        return self.descripcion