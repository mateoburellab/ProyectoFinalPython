from django import forms

class Formulario_cliente(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20)
    nro_telefono = forms.CharField(max_length = 12)
    dni = forms.IntegerField()
    nro_cliente = forms.IntegerField()

class Formulario_vendedor(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20)
    nro_telefono = forms.CharField(max_length = 12)
    dni = forms.IntegerField()
    cuit = forms.CharField(max_length = 11)

class Formulario_articulo(forms.Form):
    nombre = forms.CharField(max_length = 50)
    categoria = forms.CharField(max_length = 50)
    descripcion = forms.CharField(max_length = 200)
    precio = forms.IntegerField()