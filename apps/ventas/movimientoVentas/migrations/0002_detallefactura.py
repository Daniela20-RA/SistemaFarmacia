# Generated by Django 4.2 on 2024-09-16 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0001_initial'),
        ('productos', '0001_initial'),
        ('movimientoVentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.factura', verbose_name='Factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name_plural': 'Detalle Facturas',
            },
        ),
    ]
