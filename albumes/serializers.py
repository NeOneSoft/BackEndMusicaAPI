from rest_framework import serializers

from artistas.serializers import ArtistaSerializer
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    artista = ArtistaSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ('nombre', 'artista')


class CreateAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ('nombre', 'artista')