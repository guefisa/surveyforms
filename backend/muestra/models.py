from django.db import models


class Muestra(models.Model):
    codigo = models.CharField(max_length=32, unique=True)
    owner = models.ForeignKey('auth.User', related_name='muestras')

    class Meta:
        ordering = ('codigo',)

    def __str__(self):
        return self.codigo