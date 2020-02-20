from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Documento, Noticia
from .models import Estudiante
from .models import TCUDato
from .models import Proyecto, Pasantia

# Register your models here.
admin.site.site_header = 'Administrador de TCU'

class TCUDatoAdmin(admin.ModelAdmin):
    list_display = ('Codigo',)
    exclude = ('Codigo',)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('Identificacion', 'Nombre', 'Primer_Apellido', 'Proyecto',)
    list_filter = ('Estado', 'Proyecto',)

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Inicio',)
    list_filter = ('Inicio',)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Fecha', 'Proyecto', 'Tipo')
    list_filter = ('Tipo', 'Proyecto',)

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.unregister(Group)
admin.site.register(Noticia)
admin.site.register(Pasantia)