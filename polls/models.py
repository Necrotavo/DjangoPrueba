from django.db import models

# Create your models here.

class Proyecto(models.Model):
    Nombre = models.CharField(max_length=30)
    Estado = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=500)
    Visble = models.BooleanField(default=True)
    def __str__(self):
        return self.Nombre

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=30)
    Primer_Apellido = models.CharField(max_length=30)
    Segundo_Apellido = models.CharField(max_length=30)
    Identificacion = models.CharField(max_length=30, primary_key=True)
    Carrera = models.CharField(max_length=30)
    Correo = models.EmailField(max_length=30)
    Telefono = models.CharField(max_length=8)
    Estado = models.CharField(max_length=30)
    Horas = models.IntegerField()
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

class Documento(models.Model):
    Nombre = models.CharField(max_length=30)
    Fecha = models.DateField(auto_now=True)

    TIPO_DOCUMENTO = [
        ('RP','REPORTE'),
        ('ST','ESTUDIO'),
        ('ED','ESTADISTICA'),
    ]

    Tipo = models.CharField(max_length=2,choices=TIPO_DOCUMENTO)
    Lugar = models.CharField(max_length=30)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Enlace = models.CharField(max_length=100)

class TCUDato(models.Model):
    Profesor = models.CharField(max_length=30)
    Nombre = models.CharField(max_length=30)
    Codigo = models.CharField(max_length=10, primary_key=True)
    Telefono = models.CharField(max_length=8)
    Correo = models.EmailField(max_length=30)
    Descripcion = models.CharField(max_length=500)
    Facebook = models.CharField(max_length=100)
    Youtube = models.CharField(max_length=100)

