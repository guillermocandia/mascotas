from django.db import models


class Mascota(models.Model):
    foto = models.FileField(
        blank=False,
        null=False
    )
    nickname = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )

    nombre = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )

    votos = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ['-votos']
