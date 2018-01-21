from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import Group
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
            # Token é criado junto com a fazenda
            self.access_token = secrets.token_hex(32)
        else:
            # Token nao pode ser alterado
            self.access_token = self.__class__.objects.get(
                pk=self.pk).access_token
        super(Fazenda, self).save(*args, **kwargs)


class GestorFazenda(models.Model):
    
    usuario = models.OneToOneField(User)
    fazenda = models.ForeignKey(Fazenda)

    def __str__(self):
        return f"{self.usuario} | {self.fazenda.nome}"
    
    def save(self, *args, **kwargs):
        self.usuario.is_staff = True
        group = Group.objects.get(name=settings.GROUPS)
        if not group:
            group = Group.objects.create(name=settings.GROUPS)
        self.usuario.groups.add(group.pk)
        self.usuario.save()
        super(GestorFazenda, self).save(*args, **kwargs)

class Gado(models.Model):
    
    numero_brinco = models.CharField(max_length=50, verbose_name="Numero do Brinco")
    especificacoes = models.TextField(null=True, blank=True)
    fazenda = models.ForeignKey(Fazenda)

    def __str__(self):
        return f"{self.numero_brinco} | {self.fazenda.nome}Kg"


class Pesagem(models.Model):
    
    class Meta:
        verbose_name_plural = "Pesagens"
    
    peso = models.FloatField()
    gado = models.ForeignKey(Gado)
    data_pesagem = models.DateField()

    def __str__(self):
        return f"{self.gado.numero_brinco} | {self.peso}Kg"

