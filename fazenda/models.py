from django.db import models
from django.contrib.auth.models import User


class Fazenda(models.Model):
    
    cnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    endereco = models.TextField()


class GestorFazenda(models.Model):
    
    usuario = models.OneToOneField(User)
    fazenda = models.ForeignKey(Fazenda)


class Gado(models.Model):
    
    numero_brinco = models.CharField(max_length=50)
    peso = models.FloatField()
    especificacoes = models.TextField(null=True, blank=True)
    fazenda = models.ForeignKey(Fazenda)
