# Generated by Django 4.2.4 on 2023-10-09 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0027_alter_cliente_fecharegistro_alter_task_comentarios_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='idCliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente'),
        ),
        migrations.AddField(
            model_name='orden',
            name='idEmpleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.usuario'),
        ),
        migrations.AddField(
            model_name='orden',
            name='totalOrden',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='idCliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='idEmpleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.usuario'),
        ),
        migrations.AddField(
            model_name='venta',
            name='idOrden',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.orden'),
        ),
    ]
