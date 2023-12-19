# Generated by Django 4.2.4 on 2023-10-09 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0037_alter_ticket_idcliente_alter_ticket_idempleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='idCliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.cliente'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='idEmpleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.usuario'),
        ),
    ]
