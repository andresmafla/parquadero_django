from django import forms
from .models import carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = carro
        fields = ['placa','entrada','tipo']
        widgets = {
            'placa': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingresar numero de la placa del vehículo',
                }
            ),
            'entrada': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Fecha de ingreso del vehículo',
                }
            ),
            'tipo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Tipo de vehículo',
                }
            ),
        }