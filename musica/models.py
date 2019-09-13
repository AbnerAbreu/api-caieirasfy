from django.db import models

class Musica(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    tempo_reprodução = models.CharField(
        max_length=255,
    )
    artista = models.CharField(
        max_length=255,
    )
    genero = models.CharField(
        max_length=255,
    )
    def __str__(self):
        return self.nome