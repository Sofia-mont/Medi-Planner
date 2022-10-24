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

class Paciente(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    habitacion = models.CharField(max_length=10)
    fecha_salida=models.DateTimeField()
    novedades = models.TextField()
    enfermeras = models.ManyToManyField(Enfermera)

    class Meta:
        verbose_name="paciente"
        verbose_name_plural="pacientes"
    def __str__(self):
        return self.nombres + " " + self.apellidos

class Medicamento(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.CharField(max_length=10)
    invima = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    via_administración = models.CharField(max_length=40)
    ubicacion = models.CharField(max_length=40)

    class Meta:
        verbose_name="medicamento"
        verbose_name_plural="medicamentos"
    def __str__(self):
        return self.nombre + " " + self.cantidad
