# Generated by Django 2.1.3 on 2018-11-10 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_auto_20181109_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fotoMascota',
            field=models.ImageField(upload_to='fotos/'),
        ),
    ]
