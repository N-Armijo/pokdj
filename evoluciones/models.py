from django.db import models
from pokemones.models import Pokemon

# Create your models here.
class Evolucion(models.Model):
    pokemon_base = models.ForeignKey(Pokemon, related_name='base', on_delete=models.CASCADE)
    pokemon_evolucion = models.ForeignKey(Pokemon, related_name='evolucion', on_delete=models.CASCADE)
    nivel_necesario = models.IntegerField()

    def __str__(self):
        return f"{self.pokemon_base} -> {self.pokemon_evolucion}"