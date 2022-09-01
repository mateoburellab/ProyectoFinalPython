from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppProyecto.forms import Formulario_cliente
from AppProyecto.models import Cliente

def inicio(request):

    diccionario = {}
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def inicio2(request):

    diccionario = {}

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def formulario_cliente(request):
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
            return (render(request, "inicio.html"), {"mensaje": "Cliente creado"})
        else:
            return (render(request, "inicio.html"), {"mensaje": "Error"})
        
    else:
        formulario = Formulario_cliente()
        return (render(request, "formulario_cliente.html", {"formulario": formulario}))