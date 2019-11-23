from django.db import models

from albumes.models import Album


class Cancion(models.Model):

    titulo = models.CharField(max_length=200)
    duracion = models.CharField(max_length=10)
    orden = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
