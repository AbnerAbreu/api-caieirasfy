from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from artista.models import Artista
from musica import views
from musica.serializers import MusicaSerializer
from artista.serializers import ArtistaSerializer, ArtistaLightSerializer
from rest_framework import status
from rest_framework.response import Response

class ArtistaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = MusicaSerializer
    queryset = Artista.objects.all()
    search_fields = ['^nome', '=idade', '=estilo_musical']
    filter_backends = [SearchFilter]

class ArtistaList(views.APIView):
    def get(self, request):
            artista = Artista.objects.all()
            serializer = ArtistaSerializer(artista, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ArtistaDetails(views.APIView):

    def get_object(self, id):
        try:
            return Artista.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        aluno = self.get_object(id)
        serializer = ArtistaLightSerializer(aluno)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        artista = self.get_object(id)
        serializer = ArtistaSerializer(artista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)