from django.contrib import admin
from apps.laboratorio.movimientosLaboratorio.models import Estado
# Register your models here.

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'tipoEstado']