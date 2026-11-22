# Sistema de Inventarios

## Descripción
Sistema web desarrollado como proyecto académico para apoyar la gestión de inventarios en minimercados de Floridablanca, Santander.

## Tecnologías
- Python
- Django
- SQLite
- HTML y CSS

## Funcionalidades
- Autenticación de usuarios.
- Gestión de productos.
- Registro de entradas y salidas.
- Actualización de existencias.
- Control de stock mínimo.
- Panel principal con indicadores.
- Consulta de reportes de movimientos.

## Instalación y ejecución

1. Clonar el repositorio:

   git clone https://github.com/gjbenavides18/SistemaInventarios.git

2. Ingresar a la carpeta:

   cd SistemaInventarios

3. Crear y activar el entorno virtual:

   python -m venv venv

   En Windows PowerShell:

   .\venv\Scripts\Activate.ps1

4. Instalar las dependencias:

   pip install -r requirements.txt

5. Ejecutar las migraciones:

   python manage.py migrate

6. Crear un usuario administrador:

   python manage.py createsuperuser

7. Iniciar el servidor:

   python manage.py runserver

8. Abrir en el navegador:

   http://127.0.0.1:8000/login/

## Repositorio
https://github.com/gjbenavides18/SistemaInventarios
