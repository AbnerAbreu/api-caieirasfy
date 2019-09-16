from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

from artista import views
from musica.models import Musica
from musica.serializers import MusicaSerializer, MusicaLightSerializer


class MusicaViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = MusicaSerializer
    queryset = Musica.objects.all()
    search_fields = ['^nome', '@tempo_reprodução', '=genero', '^artista']
    filter_backends = [SearchFilter]

class MusicaList(views.APIView):
    def get(self, request):
            musica = Musica.objects.all()
            serializer =MusicaSerializer(musica, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MusicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class MusicaDetails(views.APIView):

    def get_object(self, id):
        try:
            return Musica.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        musica = self.get_object(id)
        serializer = MusicaLightSerializer(musica)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        musica = self.get_object(id)
        serializer = MusicaSerializer(musica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)