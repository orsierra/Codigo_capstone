# Generated by Django 4.1.8 on 2024-10-14 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_merge_20241014_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(default='Sin apellido', max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='apoderado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alumnos', to='core.apoderado'),
        ),
    ]
