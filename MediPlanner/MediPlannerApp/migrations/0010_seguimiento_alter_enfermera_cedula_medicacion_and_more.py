# Generated by Django 4.1 on 2022-10-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediPlannerApp', '0009_medicamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'seguimiento',
                'verbose_name_plural': 'seguimiento',
            },
        ),
        migrations.AlterField(
            model_name='enfermera',
            name='cedula',
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Medicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('dosis', models.CharField(max_length=50)),
                ('medicamento', models.ManyToManyField(to='MediPlannerApp.medicamento')),
                ('seguimiento', models.ManyToManyField(to='MediPlannerApp.seguimiento')),
            ],
            options={
                'verbose_name': 'medicacion',
                'verbose_name_plural': 'medicacion',
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='medicacion',
            field=models.ManyToManyField(to='MediPlannerApp.medicacion'),
        ),
    ]