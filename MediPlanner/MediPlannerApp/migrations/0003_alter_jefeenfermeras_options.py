# Generated by Django 4.1.2 on 2022-10-07 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MediPlannerApp', '0002_alter_enfermera_options_alter_enfermera_cedula_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jefeenfermeras',
            options={'verbose_name': 'Jefe', 'verbose_name_plural': 'Jefes'},
        ),
    ]