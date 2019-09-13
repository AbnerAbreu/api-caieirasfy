from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from musica.models import Musica
from musica.serializers import MusicaSerializer


class MusicaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = MusicaSerializer
    queryset = Musica.objects.all()
    search_fields = ['^nome', '@tempo_reprodução', '=genero', '^artista']
    filter_backends = [SearchFilter]