from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    nro_telefono = models.CharField(max_length = 12)
    dni = models.IntegerField()
    nro_cliente = models.IntegerField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    nro_telefono = models.CharField(max_length = 12)
    dni = models.IntegerField()
    cuit = models.CharField(max_length = 11)

class Articulo(models.Model):
    nombre = models.CharField(max_length = 50)
    categoria = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 200)
    precio = models.IntegerField()