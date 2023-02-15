# Generated by Django 4.1.6 on 2023-02-08 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200)),
                ('modelo', models.CharField(max_length=200, null=True)),
                ('imagen', models.ImageField(upload_to='revistaCamiones', verbose_name='foto camion')),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación ')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('categorias', models.ManyToManyField(to='revistaCamiones.categorias', verbose_name='categorias')),
            ],
            options={
                'verbose_name': 'camion',
                'verbose_name_plural': 'camiones',
                'ordering': ['-created'],
            },
        ),
    ]