# Generated by Django 2.1.3 on 2018-11-09 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0009_auto_20181108_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='region',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='vivienda',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default='Usuario', max_length=20),
        ),
    ]
