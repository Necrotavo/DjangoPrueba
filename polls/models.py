from django.db import models

# Create your models here.

class Proyecto(models.Model):
    Nombre = models.CharField(max_length=70)
    Estado = models.CharField(max_length=70)
    Descripcion = models.CharField(max_length=700)
    Imagen = models.ImageField(upload_to='polls/images')
    Visible = models.BooleanField(default=True)
    def __str__(self):
        return self.Nombre

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=70)
    Primer_Apellido = models.CharField(max_length=70)
    Segundo_Apellido = models.CharField(max_length=70)
    Identificacion = models.CharField(max_length=30, primary_key=True)
    Carrera = models.CharField(max_length=70)
    Correo = models.EmailField(max_length=70)
    Telefono = models.CharField(max_length=8)
    Estado = models.CharField(max_length=30)
    Horas = models.IntegerField()
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nombre + " " + self.Primer_Apellido + " " + self.Segundo_Apellido

class Documento(models.Model):
    Nombre = models.CharField(max_length=150)
    Fecha = models.DateField(auto_now=True)
#cambios
    TIPO_DOCUMENTO = [
        ('RP','REPORTE'),
        ('ST','ESTUDIO'),
        ('ED','ESTADISTICA'),
    ]

    Tipo = models.CharField(max_length=2,choices=TIPO_DOCUMENTO)
    Lugar = models.CharField(max_length=70)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Enlace = models.CharField(max_length=300)
    def __str__(self):
        return self.Nombre

class TCUDato(models.Model):
    Profesor = models.CharField(max_length=210)
    Nombre = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=20, primary_key=True)
    Telefono = models.CharField(max_length=8)
    Correo = models.EmailField(max_length=70)
    Descripcion = models.CharField(max_length=500)
    Facebook = models.CharField(max_length=200)
    Youtube = models.CharField(max_length=200)
    def __str__(self):
        return self.Nombre

class Noticia(models.Model):
    Descripcion = models.CharField(max_length=1000)
    Titulo = models.CharField(max_length=100)
    Imagen = models.ImageField(upload_to='polls/images')
    Identificacion = models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return self.Titulo