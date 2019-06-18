from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50, null=False)
    categoria = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    descricao = models.CharField(max_length=50, null=False)
    preco = models.FloatField(null=False)
    marca = models.ForeignKey(Marca)

    def __str__(self):
        return self.descricao
