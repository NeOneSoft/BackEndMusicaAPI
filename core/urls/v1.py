from django.conf.urls import url, include

from rest_framework import routers

from albumes.views import AlbumViewSet
from artistas.views import ArtistaViewSet
from canciones.views import CancionViewSet

routers = routers.DefaultRouter()
routers.register(r'artistas', ArtistaViewSet)
routers.register(r'albumes', AlbumViewSet)
routers.register(r'canciones', CancionViewSet)

urlpatterns = [
    url(r'', include(routers.urls))
]