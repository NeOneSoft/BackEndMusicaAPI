from django.db import models

from artistas.models import Artista


class Album(models.Model):
    nombre = models.CharField(max_length=200)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre