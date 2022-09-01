"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppProyecto.views import inicio, home_clientes, home_vendedores, home_articulos, form_clientes, form_vendedores, form_articulos, busqueda_cliente, resultado_clientes, busqueda_articulo, resultado_articulos, busqueda_vendedor, resultado_vendedores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name = 'inicio'),
    
    path('home_clientes/', home_clientes, name = 'home_clientes'),
    path('form_clientes/', form_clientes, name = 'form_clientes'),
    path('busqueda_cliente/', busqueda_cliente, name = 'busqueda_cliente'),
    path('resultado_clientes/', resultado_clientes, name = 'resultado_clientes'),

    path('home_vendedores/', home_vendedores, name = 'home_vendedores'),
    path('form_vendedores/', form_vendedores, name = 'form_vendedores'),
    path('busqueda_vendedor/', busqueda_vendedor, name = 'busqueda_vendedor'),
    path('resultado_vendedores/', resultado_vendedores, name = 'resultado_vendedores'),

    path('home_articulos/', home_articulos, name = 'home_articulos'),
    path('form_articulos/', form_articulos, name = 'form_articulos'),
    path('busqueda_articulo/', busqueda_articulo, name = 'busqueda_articulo'),
    path('resultado_articulos/', resultado_articulos, name = 'resultado_articulos'),
]
