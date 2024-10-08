# Generated by Django 5.0.3 on 2024-04-04 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MachineName', models.CharField(max_length=255)),
                ('MachineID', models.CharField(max_length=10, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MachineIDString', models.CharField(blank=True, max_length=10)),
                ('Id_parameter', models.CharField(blank=True, max_length=10)),
                ('value', models.FloatField()),
                ('time', models.FloatField()),
                ('MachineID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datamanagement.machine')),
            ],
        ),
    ]
