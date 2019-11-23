from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from canciones.models import Cancion
from canciones.serializers import CancionSerializer, CreateCancionSerializer


class CancionViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de una cancion  de acuerdo al ID generado.
    list:
        Regresa la lista de canciones en la base de datos
    create:
        Crea una cancion en la base de datos
    delete:
        Elimina una cancion
    update:
        Actualiza una cancion
    """
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCancionSerializer
        return CancionSerializer

    @action(detail=True, methods=['GET'])
    def albumes(self, request, pk=None):
        cancion = self.get_object()
        albumes = Cancion.objects.filter(album=cancion.id)
        serialized = CancionSerializer(albumes, many=True)
        if not albumes:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Esta cancion no esta asignada a un album'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)






