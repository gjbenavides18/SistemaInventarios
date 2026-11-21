
from django.shortcuts import render
from django.db import models
from django.contrib.auth.decorators import login_required
from .models import Producto, MovimientoInventario


@login_required
def inicio(request):
    total_productos = Producto.objects.filter(activo=True).count()

    productos_stock_bajo = Producto.objects.filter(
        activo=True,
        stock_actual__lte=models.F('stock_minimo')
    ).count()

    total_movimientos = MovimientoInventario.objects.count()

    contexto = {
        'total_productos': total_productos,
        'productos_stock_bajo': productos_stock_bajo,
        'total_movimientos': total_movimientos,
    }

    return render(
        request,
        'inventario_productos/inicio.html',
        contexto
    )


@login_required
def reporte_movimientos(request):
    movimientos = MovimientoInventario.objects.select_related(
        'producto', 'usuario'
    ).all().order_by('-fecha')

    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio:
        movimientos = movimientos.filter(fecha__date__gte=fecha_inicio)

    if fecha_fin:
        movimientos = movimientos.filter(fecha__date__lte=fecha_fin)

    contexto = {
        'movimientos': movimientos,
        'fecha_inicio': fecha_inicio or '',
        'fecha_fin': fecha_fin or '',
    }

    return render(
        request,
        'inventario_productos/reporte_movimientos.html',
        contexto
    )
