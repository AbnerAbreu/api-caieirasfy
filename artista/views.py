from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from artista.models import Artista
from musica.serializers import MusicaSerializer


class ArtistaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = MusicaSerializer
    queryset = Artista.objects.all()
    search_fields = ['^nome', '=idade', '=estilo_musical']
    filter_backends = [SearchFilter]
