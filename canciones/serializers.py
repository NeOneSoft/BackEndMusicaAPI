from rest_framework import serializers

from albumes.serializers import AlbumSerializer
from .models import Cancion


class CancionSerializer(serializers.ModelSerializer):
    """
    General purpose
    """
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Cancion
        fields = ('titulo', 'duracion', 'orden', 'album')


class CreateCancionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cancion
        fields = ('titulo', 'duracion', 'orden', 'album')