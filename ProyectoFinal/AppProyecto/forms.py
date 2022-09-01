from django import forms

class Formulario_cliente(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20)
    nro_telefono = forms.CharField(max_length = 12)
    dni = forms.IntegerField()
    nro_cliente = forms.IntegerField()