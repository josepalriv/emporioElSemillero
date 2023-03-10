# Generated by Django 4.1.5 on 2023-01-29 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "categoria",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Categoría"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Presentacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipoPresentacion",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Tipo de Presentación"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    models.IntegerField(unique=True, verbose_name="Código de Producto"),
                ),
                (
                    "nombre",
                    models.CharField(max_length=100, verbose_name="Nombre de Producto"),
                ),
                (
                    "contenido",
                    models.CharField(max_length=50, verbose_name="Tipo de Contenido"),
                ),
                (
                    "precioVenta",
                    models.IntegerField(verbose_name="Precio de Venta a Público"),
                ),
                (
                    "foto",
                    models.ImageField(blank=True, null=True, upload_to="img_productos"),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.categoria",
                    ),
                ),
                (
                    "presentacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.presentacion",
                    ),
                ),
            ],
        ),
    ]
