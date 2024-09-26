from django.db import models

#Tipo DE FACTURA
class TipoFacturas(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique=True)
    descripcion = models.CharField(verbose_name='Tipo de compra', max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo de factura'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    
class DetalleFactura(models.Model):
    #models.CASCADE significa que en el caso que se elimine una factura todos los detalles relacionados tambien se eleminaran
    factura = models.ForeignKey('facturas.Factura', verbose_name='Factura', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', verbose_name='Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle Facturas'

    def __str__(self):
        return f"Factura: {self.factura.codigo}, Producto: {self.producto.nombreProducto}, Cantidad: {self.cantidad}, Precio: {self.precio}"

