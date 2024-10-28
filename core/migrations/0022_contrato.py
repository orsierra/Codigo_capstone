# Generated by Django 5.1.1 on 2024-10-25 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_firma', models.DateField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_pago', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('apoderado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos', to='core.apoderado')),
            ],
        ),
    ]