# Generated by Django 4.1.5 on 2023-01-24 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetario', '0002_rename_recetario_recetas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Recetas',
            new_name='Receta',
        ),
    ]
