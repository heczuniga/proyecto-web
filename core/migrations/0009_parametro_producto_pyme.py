# Generated by Django 3.1 on 2022-11-04 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_auto_20221103_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('codParametro', models.AutoField(primary_key=True, serialize=False, verbose_name='Código del parámetro')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre (*)')),
                ('valor', models.CharField(max_length=100, verbose_name='Valor (*)')),
            ],
        ),
        migrations.CreateModel(
            name='Pyme',
            fields=[
                ('idPyme', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de la PYME')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la PYME')),
                ('rut', models.CharField(max_length=100, verbose_name='RUT de la PYME')),
                ('sitioWeb', models.CharField(max_length=200, null=True, verbose_name='Sitio web de la fundación')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fundaciones', verbose_name='Imagen de la fundación')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del producto (*)')),
                ('nombreCorto', models.CharField(max_length=100, verbose_name='Nombre corto del producto (*)')),
                ('nombreLargo', models.CharField(max_length=200, verbose_name='Nombre largo del producto (*)')),
                ('descripcion', models.TextField(max_length=1000, verbose_name='Descripción del producto (*)')),
                ('precio', models.IntegerField(verbose_name='Precio del producto (*)')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Imagen del producto (*)')),
                ('pyme', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='core.pyme', verbose_name='PYME que vende el producto (*)')),
            ],
        ),
    ]