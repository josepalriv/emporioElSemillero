from django.db import models


# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True, verbose_name="Categoría")

    def __str__(self):
        return self.categoria


class Presentacion(models.Model):
    tipoPresentacion = models.CharField(max_length=20, unique=True, verbose_name="Tipo de Presentación")

    def __str__(self):
        return self.tipoPresentacion


class Contenido(models.Model):
    tipoContenido = models.CharField(max_length=50, unique=True, verbose_name="Tipo de Contenido")

    def __str__(self):
        return self.tipoContenido


class Producto(models.Model):
    codigo = models.IntegerField(unique=True, verbose_name="Código de Producto")
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    contenido = models.ForeignKey(Contenido, on_delete=models.DO_NOTHING)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.DO_NOTHING)
    precioVenta = models.IntegerField(verbose_name="Precio de Venta a Público")
    foto = models.ImageField(height_field=None, width_field=None, verbose_name="Imagen del Producto")

    def __str__(self):
        return self.nombre
