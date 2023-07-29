from django.db import models


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11, unique=True)


class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente, models.CASCADE)
    data = models.DateField()
    observacao = models.TextField(blank=True)


class ItemPedido(models.Model):

    pedido = models.ForeignKey(Pedido, models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
