import os
import importlib
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from django.conf import settings
from subprocess import call
from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import ContentType
from django.contrib.auth.models import Group
from django.db.models.query import QuerySet
import collections


class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        try:
            group = Group.objects.get(name=settings.GROUPS)
        except:
            group = Group.objects.create(name=settings.GROUPS)
        self.make_permissions()
        
    def set_permission(self, groups, permissions):
        for group in groups:
            db_group = Group.objects.get(name=group)
            print('-->Group{0}: --> Permissions{1}'.format(groups, permissions) )
            for permission in permissions:
                if isinstance(permission, QuerySet):
                    permission = permission.first()
                db_group.permissions.add(permission)

    def get_content_type_permissions(self, data):
        ct = ContentType.objects.get(model=data.model_name)

        if data.permissions.__contains__('all'):
            self.set_permission(data.groups, ct.permission_set.all())
        else:
            permissions = []
            for codename in data.permissions:
                permissions.append(ct.permission_set.filter(
                    codename__icontains=codename))
            self.set_permission(data.groups, permissions)

    def make_permissions(self, *args, **kwargs):
        """
        Tupla nomeada é possivel assim passar o model_name os grupos
        Grupos Validos ['GESTORES_FAZENDAS'] ...
        
        """
        ModelPermissions = collections.namedtuple(
            'ModelPermissions', 'model_name groups permissions')

        # Gestores Grupos
        groups = [settings.GROUPS]

        models_with_permissions = [
            
            ModelPermissions('fazenda', groups, ['add', 'change']),
            ModelPermissions('gado', groups, ['all']),
            ModelPermissions('pesagem', groups, ['all']),

        ]

        for model in models_with_permissions:
            self.get_content_type_permissions(model)