from django.db import models
from django.core.validators import MinValueValidator


class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=100)
    correo = models.EmailField()
    monto = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
        ordering = ("nombre",)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20)
    precio = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        validators=[MinValueValidator(0)],
    )
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name="libros",
    )

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ("titulo",)

    def __str__(self):
        return self.titulo
