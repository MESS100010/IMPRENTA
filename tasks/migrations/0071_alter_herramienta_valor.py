# Generated by Django 4.2.5 on 2023-10-11 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0070_herramienta_idproveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herramienta',
            name='valor',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
