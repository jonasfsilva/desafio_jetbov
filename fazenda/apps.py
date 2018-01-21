from django.apps import AppConfig
from django.db.models.signals import post_migrate
from subprocess import call
from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import Group

def get_or_create_gestores_group(sender, *args, **kwargs):
    try:
        group = Group.objects.get(name=settings.GROUPS)
    except:
        group = Group.objects.create(name=settings.GROUPS)

def set_permissions(sender, *args, **kwargs):
    call_command('set_permissions')


class FazendaConfig(AppConfig):
    name = 'fazenda'
    verbose_name = 'Fazenda JetBov'

    def ready(self):
        print('Criando Grupo')
        post_migrate.connect(get_or_create_gestores_group, sender=self)
        post_migrate.connect(set_permissions, sender=self)
