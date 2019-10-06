from django.db import models
from django.urls import reverse

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros'),
)


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    imagem = models.ImageField(upload_to='pessoas', null=True, blank=True)

    class Meta:
        ordering = ['nome', ]
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome
    
    def get_sexo(self):
        if self.sexo == 'M':
            return 'Masculino'
        elif self.sexo == 'F':
            return 'Feminino'
        else:
            return 'Outros'

    def get_absolute_url(self):
        return reverse("pessoa_detail", kwargs={"pk": self.pk})