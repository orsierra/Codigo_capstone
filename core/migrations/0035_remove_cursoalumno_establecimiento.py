# Generated by Django 5.1.3 on 2024-11-13 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_sostenedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursoalumno',
            name='establecimiento',
        ),
    ]
