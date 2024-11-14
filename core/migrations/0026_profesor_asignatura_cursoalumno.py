# Generated by Django 5.1.1 on 2024-11-04 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_asismatricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='asignatura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='CursoAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curso_alumno_relacion', to='core.alumno')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='curso_alumno_relacion', to='core.curso')),
            ],
            options={
                'verbose_name': 'Relación Curso-Alumno',
                'verbose_name_plural': 'Relaciones Curso-Alumno',
                'unique_together': {('curso', 'alumno')},
            },
        ),
    ]