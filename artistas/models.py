from django.db import models




class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

