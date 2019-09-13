from rest_framework import serializers
from artista.models import Artista

from musica.models import Musica

class ArtistaSerializer(serializers.Serializer):
    id = serializers.intergeField()
    nome = serializers.Charfield(read_only=True)

class MusicaSerializer(serializers.Serializer):
    id = serializers.intergeField()
    nome = serializers.Charfield(max_length=255,required=True)
    idade = serializers.intergeField()
    estilo_musical = serializers.Charfield()

    def create(self, validated_data):
        musica_data = validated_data.pop('estilo_musical')
        musica = Musica.objects.get(id=musica_data['id'])
        artista = Artista.objects.create(estilo_musical=Musica, **validated_data)
        return artista

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.email = validated_data.get('estilo_musical')
        musica = Musica.objects.get(id=musica_data['id'])
        instance.estilo_musical = musica
        instance.save()
        return instance


class ArtistaLightSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)
