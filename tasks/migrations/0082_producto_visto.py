# Generated by Django 4.2.5 on 2023-10-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0081_usuario_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
