from django.db import models

#Tipo DE COMPRA
class TipoDeCompras(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=10, unique=True)
    descripcion = models.CharField(verbose_name='Tipo de compra', max_length=50)

    class Meta:
        verbose_name_plural = 'Tipo de compras'

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
    

#DETALLE DE COMPRA 
class DetallesCompras(models.Model):
    compra = models.ForeignKey('compras.Compra', verbose_name='Compra', on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', verbose_name='Producto', on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.FloatField(verbose_name='Precio')

    class Meta:
        verbose_name_plural = 'Detalle Compras'

    def __str__(self):
        return f"Compras: {self.compra.codigo}, Producto: {self.producto.nombreProducto}, Cantidad: {self.cantidad}, Precio: {self.precio}"



