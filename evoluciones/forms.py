from django import forms
from .models import Evolucion

class EvolucionForm(forms.ModelForm):
    class Meta:
        model = Evolucion
        fields = ['pokemon_base', 'nivel_necesario', 'pokemon_evolucion']
        labels = {
            'pokemon_base': 'Pokemon Base',
            'nivel_necesario': 'Nivel Necesario',
            'pokemon_evolucion': 'Pokémon Evolucionado',
        }
        widgets = {
            'pokemon_base': forms.Select(attrs={'class': 'form-select'}),
            'nivel_necesario': forms.NumberInput(attrs={'class': 'form-control'}),
            'pokemon_evolucion': forms.Select(attrs={'class': 'form-select'}),
        }
