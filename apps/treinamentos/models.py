from django.db import models

from apps.pessoas.models import Pessoa


class Treinamento(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    treinamento = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='treinamentos', null=True, blank=True)

    def __str__(self):
        return self.treinamento

    class Meta:
        verbose_name = 'Treinamento'
        verbose_name_plural = 'Treinamentos'

