# Generated by Django 4.2.7 on 2023-11-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerroBombero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('raza', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('estacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.estacion')),
            ],
        ),
    ]