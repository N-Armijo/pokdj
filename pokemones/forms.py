from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nombre', 'nivel', 'tipo']
        labels = {
            'nombre': 'Nombre del Pokémon',
            'nivel': 'Nivel',
            'tipo': 'Tipo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
        }
