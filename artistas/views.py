from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from albumes.models import Album
from albumes.serializers import AlbumSerializer
from artistas.models import Artista
from artistas.serializers import ArtistaSerializer
from canciones.models import Cancion
from canciones.serializers import CancionSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un artista  de acuerdo al ID generado.
    list:
        Regresa la lista de artistas en la base de datos
    create:
        Crea un artista en la base de datos
    delete:
        Elimina un artista
    update:
        Actualiza un artista
    """
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

    @action(detail=True, methods=['GET'])
    def canciones(self, request, pk=None):
        artista = self.get_object()
        canciones = Cancion.objects.filter(album=artista.id)
        serialized = CancionSerializer(canciones, many=True)
        if not canciones:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este artista no tiene canciones'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def albumes(self, request, pk=None):
        artista = self.get_object()
        albumes = Album.objects.filter(artista__id=artista.id)
        serialized = AlbumSerializer(albumes, many=True)
        if not albumes:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este artista no tiene albumes'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

