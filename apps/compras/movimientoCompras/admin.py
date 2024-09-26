from django.contrib import admin
from apps.compras.movimientoCompras.models import TipoDeCompras
from apps.compras.movimientoCompras.models import DetallesCompras

@admin.register(TipoDeCompras)
class TipocompraAdmin(admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ['codigo', 'descripcion']

@admin.register(DetallesCompras)
class DetalleComprasAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'cantidad', 'precio')
    search_fields = ('compra__codigo', 'producto__nombreProducto')
    list_filter = ('compra', 'producto')
