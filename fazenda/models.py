from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import secrets


class Fazenda(models.Model):
    
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    endereco = models.TextField()
    access_token = models.CharField(max_length=32)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.pk:
            self.access_token = secrets.token_hex(32)
        super(Fazenda, self).save(*args, **kwargs)


class GestorFazenda(models.Model):
    
    usuario = models.OneToOneField(User)
    fazenda = models.ForeignKey(Fazenda)

    def __str__(self):
        return f"{self.usuario} | {self.fazenda.nome}"
    
    def save(self, *args, **kwargs):
        self.usuario.is_staff = True
        self.usuario.save()
        super(GestorFazenda, self).save(*args, **kwargs)

class Gado(models.Model):
    
    numero_brinco = models.CharField(max_length=50)
    especificacoes = models.TextField(null=True, blank=True)
    fazenda = models.ForeignKey(Fazenda)

    def __str__(self):
        return f"{self.numero_brinco} | {self.fazenda.nome}Kg"


class Pesagem(models.Model):
    
    peso = models.FloatField()
    gado = models.ForeignKey(Gado)
    data_pesagem = models.DateField()

    def __str__(self):
        return f"{self.gado.numero_brinco} | {self.peso}Kg"

