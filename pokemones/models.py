from django.db import models
from tipos.models import Tipo

# Create your models here.
class Pokemon(models.Model):
    nombre= models.CharField(max_length=100)
    nivel = models.IntegerField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

