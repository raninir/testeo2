# Generated by Django 2.1 on 2018-11-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_usuario_run'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(default='', upload_to='mascotas/', verbose_name='Foto Mascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='descripcionMascota',
            field=models.CharField(default='', max_length=50, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(max_length=20, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombreMascota',
            field=models.CharField(max_length=20, verbose_name='Nombre Mascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='razaMascota',
            field=models.CharField(default='', max_length=30, verbose_name='Raza Mascota'),
        ),
    ]
