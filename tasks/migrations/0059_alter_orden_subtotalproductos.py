# Generated by Django 4.2.5 on 2023-10-11 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0058_alter_orden_preciounitario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='subtotalProductos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
