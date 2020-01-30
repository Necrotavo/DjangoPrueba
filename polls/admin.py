from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Documento
from .models import Estudiante
from .models import TCUDato
from .models import Proyecto

# Register your models here.
admin.site.site_header = 'Administrador de TCU'

class TCUDatoAdmin(admin.ModelAdmin):
    list_display = ('Codigo',)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('Identificacion', 'Nombre', 'Primer_Apellido', 'Proyecto', 'Horas',)
    list_filter = ('Proyecto',)


admin.site.register(Documento)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(TCUDato, TCUDatoAdmin)
admin.site.register(Proyecto)
admin.site.unregister(Group)