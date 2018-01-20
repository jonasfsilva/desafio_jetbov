from django.db import models
from django.contrib.auth.models import User


class Fazenda(models.Model):
    
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class GestorFazenda(models.Model):
    
    usuario = models.OneToOneField(User)
    fazenda = models.ForeignKey(Fazenda)

    def __str__(self):
        return f"{self.usuario} | {self.fazenda.nome}"

class Gado(models.Model):
    
    numero_brinco = models.CharField(max_length=50)
    peso = models.FloatField()
    especificacoes = models.TextField(null=True, blank=True)
    fazenda = models.ForeignKey(Fazenda)

    def __str__(self):
        return f"{self.numero_brinco} | {self.peso}Kg"
