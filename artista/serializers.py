from rest_framework import serializers
from artista.models import Artista


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields =('id','nome', 'idade', 'estilo_musical')
