
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='inventario_productos/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path('', views.inicio, name='inicio'),

    path(
        'reportes/',
        views.reporte_movimientos,
        name='reporte_movimientos'
    ),
]
