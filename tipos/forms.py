from django import forms
from .models import Tipo

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre del Tipo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
