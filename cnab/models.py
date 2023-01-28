from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Transactions(models.Model):
    tipo = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    data = models.DateField()#8
    valor = models.BigIntegerField()#10
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()#4
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)


class Files(models.Model):
    cnab_file = models.FileField()