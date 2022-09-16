# Generated by Django 2.1.5 on 2022-09-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='servicios',
        ),
        migrations.AddField(
            model_name='reserva',
            name='modalidad',
            field=models.CharField(choices=[('', '---------'), ('ARRIENDO', 'Arriendo'), ('Venta', 'Venta')], default=None, max_length=100),
        ),
    ]
