from django.contrib import admin
from apps.compras.compras.models import Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'fecha', 'proveedorId', 'tipoDeCompraId']

