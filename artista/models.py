from django.db import models

class Artista(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    idade = models.CharField(
        max_length=255,
    )
    estilo_musical = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.nome
