from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [

            'solicitud',
            'nombre',
            'email',
            'telefono',
            'direccion',
        ]

        labels = {
            'solicitud': 'Solicitud',
            'nombre': 'Nombre',
            'email': 'Email',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
        }