# Generated by Django 5.1.1 on 2024-10-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_merge_20241017_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='estado_admision',
            field=models.CharField(choices=[('Aprobado', 'Aprobado'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20),
        ),
    ]
