from django.db import models
from apps.compras.proveedores.models import Proveedores
from apps.compras.movimientoCompras.models import TipoDeCompras

class Compra(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=30, unique=True)
    fecha = models.DateField(verbose_name= 'Fecha')
    proveedorId = models.ForeignKey(Proveedores, verbose_name='Proveedor', on_delete=models.PROTECT)
    tipoDeCompraId = models.ForeignKey(TipoDeCompras, verbose_name='Tipo de compra', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Compras'
    
    def __str__(self):
        return f"{self.codigo}-{self.fecha}"