from django.db import models
from ..accounts.models import User


class Quarto(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    imagem = models.URLField(max_length=200, null=True)
    # imagem = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # miniatura = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def to_dict_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cidade': self.cidade,
            'valor': self.valor,
            'description': self.description,
            'imagem': self.imagem,
        }


class Likes(models.Model):
    quarto = models.ManyToManyField(Quarto)
    like = models.BooleanField(default=False)
