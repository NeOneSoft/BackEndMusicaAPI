from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from albumes.models import Album
from albumes.serializers import AlbumSerializer, CreateAlbumSerializer
from canciones.models import Cancion
from canciones.serializers import CancionSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un album  de acuerdo al ID generado.
    list:
        Regresa la lista de albumes en la base de datos
    create:
        Crea un album en la base de datos
    delete:
        Elimina un album
    update:
        Actualiza un album
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAlbumSerializer
        return AlbumSerializer

    @action(detail=True, methods=['GET'])
    def canciones(self, request, pk=None):
        album = self.get_object()
        canciones = Cancion.objects.filter(album=album.id)
        serialized = CancionSerializer(canciones, many=True)
        if not canciones:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este album no tiene canciones'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)


