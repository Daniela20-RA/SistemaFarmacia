from django.contrib import admin
from apps.laboratorio.consultas.models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'fecha', 'clienteId']

