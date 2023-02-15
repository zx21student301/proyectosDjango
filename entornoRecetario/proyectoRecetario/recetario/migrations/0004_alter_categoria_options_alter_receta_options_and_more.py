# Generated by Django 4.1.5 on 2023-01-24 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recetario', '0003_rename_categorias_categoria_rename_recetas_receta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['-created'], 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='receta',
            options={'ordering': ['-created'], 'verbose_name': 'receta', 'verbose_name_plural': 'recetas'},
        ),
        migrations.AddField(
            model_name='categoria',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categoria',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AddField(
            model_name='receta',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receta',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receta',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='recetario', verbose_name='Foto receta'),
        ),
    ]