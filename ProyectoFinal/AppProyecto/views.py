from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppProyecto.forms import Formulario_cliente, Formulario_vendedor, Formulario_articulo
from AppProyecto.models import Cliente, Vendedor, Articulo

def inicio(request):

    diccionario = {}
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def home_vendedores(request):
    diccionario = {}
    plantilla = loader.get_template("home_vendedores.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def home_articulos(request):
    diccionario = {}
    plantilla = loader.get_template("home_articulos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def home_clientes(request):
    diccionario = {}
    plantilla = loader.get_template("home_clientes.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def form_clientes(request):
    if (request.method == "POST"):
        formulario = Formulario_cliente(request.POST)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            nombre1 = info.get("nombre")
            apellido1 = info.get("apellido")
            nro_telefono1 = info.get("nro_telefono")
            dni1 = info.get("dni")
            nro_cliente1 = info.get("nro_cliente")
            cliente = Cliente(nombre = nombre1, apellido = apellido1, nro_telefono = nro_telefono1, dni = dni1, nro_cliente = nro_cliente1)
            cliente.save()
            return (render(request, "inicio.html", {"mensaje": "Cliente creado"}))
        else:
            return (render(request, "inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_cliente()
        return (render(request, "form_clientes.html", {"formulario": formulario}))

def form_vendedores(request):
    if (request.method == "POST"):
        formulario = Formulario_vendedor(request.POST)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            nombre1 = info.get("nombre")
            apellido1 = info.get("apellido")
            nro_telefono1 = info.get("nro_telefono")
            dni1 = info.get("dni")
            cuit1 = info.get("cuit")
            vendedor = Vendedor(nombre = nombre1, apellido = apellido1, nro_telefono = nro_telefono1, dni = dni1, cuit = cuit1)
            vendedor.save()
            return (render(request, "inicio.html", {"mensaje": "Vendedor creado"}))
        else:
            return (render(request, "inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_vendedor()
        return (render(request, "form_vendedores.html", {"formulario": formulario}))

def form_articulos(request):
    if (request.method == "POST"):
        formulario = Formulario_articulo(request.POST)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            nombre1 = info.get("nombre")
            categoria1 = info.get("categoria")
            descripcion1 = info.get("descripcion")
            precio1 = info.get("precio")
            articulo = Articulo(nombre = nombre1, categoria = categoria1, descripcion = descripcion1, precio = precio1)
            articulo.save()
            return (render(request, "inicio.html", {"mensaje": "Articulo creado"}))
        else:
            return (render(request, "inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_articulo()
        return (render(request, "form_articulos.html", {"formulario": formulario}))

def busqueda_cliente(request):
    return (render(request, "busqueda_cliente.html"))

def resultado_clientes(request):
    if (request.GET.get("nro_cliente")):
        nro_cliente = request.GET.get("nro_cliente")
        clientes = Cliente.objects.filter(nro_cliente = nro_cliente)
        if (len(clientes) != 0):
            return (render(request, "resultados_clientes.html", {"clientes": clientes}))
        else:
            return render(request, "resultados_clientes.html", {"mensaje": "Cliente(s) no encontrado(s)"})
    else:
        return (render(request, "busqueda_cliente.html", {"mensaje": "Por favor, ingrese un numero de cliente"}))

def busqueda_vendedor(request):
    return (render(request, "busqueda_vendedor.html"))

def resultado_vendedores(request):
    if (request.GET.get("cuit")):
        cuit1 = request.GET.get("cuit")
        vendedores = Vendedor.objects.filter(cuit = cuit1)
        if (len(vendedores) != 0):
            return (render(request, "resultados_vendedores.html", {"vendedores": vendedores}))
        else:
            return render(request, "resultados_vendedores.html", {"mensaje": "Vendedor(es) no encontrado(s)"})
    else:
        return (render(request, "busqueda_vendedor.html", {"mensaje": "Por favor, ingrese un numero de CUIT del vendedor"}))

def busqueda_articulo(request):
    return (render(request, "busqueda_articulo.html"))

def resultado_articulos(request):
    if (request.GET.get("categoria")):
        categoria = request.GET.get("categoria")
        articulos = Articulo.objects.filter(categoria = categoria)
        if (len(articulos) != 0):
            return (render(request, "resultados_articulos.html", {"articulos": articulos}))
        else:
            return render(request, "resultados_articulos.html", {"mensaje": "Articulo(s) no encontrado(s)"})
    else:
        return (render(request, "busqueda_articulo.html", {"mensaje": "Por favor, ingrese una categoria de Articulo"}))