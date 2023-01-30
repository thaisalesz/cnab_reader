from django.db import models


# Create your models here.

class Transaction_Type(models.IntegerChoices):
    DEBITO = 1, ('Débito')
    BOLETO = 2, ('Boleto')
    FINANCIAMENTO = 3, ('Financiamento')
    CREDITO = 4, ('Crédito')
    RECEBIMENTO_EMPRESTIMO = 5, ('Recebimento Emprestimo')
    VENDAS = 6, ('Vendas')
    RECEBIMENTO_TED = 7, ('Recebimento TED')
    RECEBIMENTO_DOC = 8, ('Recebimento DOC')
    ALUGUEL = 9, ('Aluguel')

class Transaction(models.Model):
    tipo = models.IntegerField(
        choices=Transaction_Type.choices
    )
    data = models.DateField()#8
    valor = models.BigIntegerField()#10
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()#4
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)

