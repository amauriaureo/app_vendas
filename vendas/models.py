from django.db import models


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True)


class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente, models.CASCADE)
    data = models.DateField()
    observacao = models.TextField(blank=True)
