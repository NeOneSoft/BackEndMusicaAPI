from rest_framework import serializers
from .models import Artista

class ArtistaSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    class Meta:
        model = Artista
        fields = ('nombre', 'fecha_nacimiento', 'genero', 'ciudad')