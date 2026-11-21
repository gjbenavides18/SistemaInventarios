
from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, MovimientoInventario


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'categoria',
        'precio_compra',
        'precio_venta',
        'stock_actual',
        'stock_minimo',
        'estado_stock',
        'activo',
    )
    search_fields = ('codigo', 'nombre')
    list_filter = ('categoria', 'activo')

    @admin.display(description='Estado del stock')
    def estado_stock(self, obj):
        if obj.stock_actual <= obj.stock_minimo:
            return format_html(
                '<span style="color: red; font-weight: bold;">{}</span>',
                'REQUIERE REPOSICIÓN'
            )
        return format_html(
            '<span style="color: green; font-weight: bold;">{}</span>',
            'DISPONIBLE'
        )


@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo', 'cantidad', 'fecha', 'usuario')
    list_filter = ('tipo', 'fecha')
    search_fields = ('producto__nombre', 'producto__codigo')

    # El usuario no se selecciona manualmente.
    exclude = ('usuario',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
