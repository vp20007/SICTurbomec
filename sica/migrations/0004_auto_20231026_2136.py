# Generated by Django 3.2 on 2023-10-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sica', '0003_ordendeproduccion_precio_materiaprima'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendeproduccion',
            name='numero_Pedido',
            field=models.IntegerField(verbose_name='N° de Pedido '),
        ),
        migrations.AlterField(
            model_name='ordendeproduccion',
            name='precio_MateriaPrima',
            field=models.FloatField(verbose_name='Precio de materia prima'),
        ),
    ]
