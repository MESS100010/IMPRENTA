# Generated by Django 4.2.5 on 2023-10-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_incidentelaboral_delete_incidenteslaborales'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opionion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('FechaRegistro', models.DateField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('calificacion', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
