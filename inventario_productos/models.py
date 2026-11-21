
from django.db import models, transaction
from django.core.exceptions import ValidationError


class Producto(models.Model):
    codigo = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    precio_compra = models.DecimalField(max_digits=12, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2)
    stock_actual = models.PositiveIntegerField(default=0)
    stock_minimo = models.PositiveIntegerField(default=5)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class MovimientoInventario(models.Model):

    TIPOS_MOVIMIENTO = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='movimientos'
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPOS_MOVIMIENTO
    )

    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    observacion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} - {self.cantidad}"

    def save(self, *args, **kwargs):

        if self.pk:
            raise ValidationError(
                "Los movimientos registrados no se pueden modificar."
            )

        if self.cantidad <= 0:
            raise ValidationError(
                "La cantidad debe ser mayor que cero."
            )

        with transaction.atomic():

            producto = Producto.objects.select_for_update().get(
                pk=self.producto_id
            )

            if not producto.activo:
                raise ValidationError(
                    "No se pueden registrar movimientos de productos inactivos."
                )

            if self.tipo == 'ENTRADA':
                producto.stock_actual += self.cantidad

            elif self.tipo == 'SALIDA':

                if self.cantidad > producto.stock_actual:
                    raise ValidationError(
                        "No hay existencias suficientes para esta salida."
                    )

                producto.stock_actual -= self.cantidad

            else:
                raise ValidationError("Tipo de movimiento no válido.")

            producto.save(update_fields=['stock_actual'])

            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError(
            "Los movimientos registrados no se pueden eliminar."
        )
