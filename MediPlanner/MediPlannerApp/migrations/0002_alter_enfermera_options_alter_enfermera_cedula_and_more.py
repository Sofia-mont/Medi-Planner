# Generated by Django 4.1.2 on 2022-10-07 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MediPlannerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enfermera',
            options={'verbose_name': 'enfermera', 'verbose_name_plural': 'enfermeras'},
        ),
        migrations.AlterField(
            model_name='enfermera',
            name='cedula',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jefeenfermeras',
            name='cedula',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]