# Generated by Django 4.2.5 on 2023-11-01 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0084_compra_idproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='idOrden',
        ),
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.producto'),
        ),
    ]
