from django.contrib import admin
from apps.ventas.movimientoVentas.models import TipoFacturas
from apps.ventas.movimientoVentas.models import DetalleFactura

@admin.register(TipoFacturas)
class TipocompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion']

@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'precio')
    search_fields = ('factura__codigo', 'producto__nombreProducto')
    list_filter = ('factura', 'producto')