# Generated by Django 4.0.3 on 2022-04-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_direccion_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='tipo_via',
        ),
        migrations.AlterField(
            model_name='direccion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
