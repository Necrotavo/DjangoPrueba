from django.shortcuts import render
from django.http import HttpResponse
from .models import TCUDato, Estudiante
from django.shortcuts import render

# Create your views here.
def index(request):
    Datos_TCU = TCUDato.objects.get(pk='TCU1515')
    Estudiantes = Estudiante.objects.all()
    context = {
        'Datos_TCU': Datos_TCU,
        'Estudiantes': Estudiantes,
    }
    return render(request, 'polls/index.html', context)


    
def detalle_Estudiante(request, student_id):
    Estudiantes = Estudiante.objects.get(pk=student_id)
    context = {
        'Estudiantes': Estudiantes,
    }
    return render(request, 'polls/detalle_Estudiante.html', context)