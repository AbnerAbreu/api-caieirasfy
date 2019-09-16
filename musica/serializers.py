from rest_framework import serializers
from musica.models import Musica

from artista.models import Artista

class MusicaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.Charfield(read_only=True)

class ArtistaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.Charfield(max_length=255,required=True)
    tempo_reprodução = serializers.IntegerField()
    genero_musical = serializers.Charfield()

    def create(self, validated_data):
        artista_data = validated_data.pop('genero_musical')
        artista = Artista.objects.get(id=artista_data['id'])
        musica = Musica.objects.create(genero_musical=Artista, **validated_data)
        return musica

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('tempo_reprodução')
        instance.email = validated_data.get('genero_musical')
        artista = Musica.objects.get(id=musica_data['id'])
        instance.genero_musical = artista
        instance.save()
        return instance


class MusicaLightSerializer(serializers.Serializer):m
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)
