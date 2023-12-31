# Generated by Django 4.2.5 on 2023-10-11 01:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0066_compra_idorden_alter_opionion_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='herramienta',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='opionion',
            name='calificacion',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
