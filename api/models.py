from django.db import models
from django.dispatch import receiver

class Emprestimo(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=15, null=False)
    endereco = models.CharField(max_length=100, null=False)
    valor_emprestimo = models.FloatField(null=True)
    status = models.CharField(max_length=10, default='Aguardando') 
    

class Protocol(models.Model):
    protocol = models.CharField(max_length=10, null=False)
    status = models.CharField(max_length=10, default='Aguardando')