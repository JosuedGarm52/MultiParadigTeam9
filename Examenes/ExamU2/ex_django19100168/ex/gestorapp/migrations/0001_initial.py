# Generated by Django 4.2.7 on 2023-11-06 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=25)),
                ('pais', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('niv', models.IntegerField()),
                ('estacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.estacion')),
            ],
        ),
        migrations.CreateModel(
            name='Bombero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('no_empleado', models.IntegerField()),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.equipo')),
            ],
        ),
    ]
