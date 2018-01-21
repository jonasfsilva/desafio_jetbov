from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from fazenda.models import Fazenda
from django.conf import settings

class JetBovTestCase(APITestCase):
    """
        Testes de toda a aplicação, geralmente divido testes
        unitarios por model, todavia desta vez coloquei todos
        os tests da aplicacao em um so canto:
        obj: Gostaria de ter feito mais tests e colocar coverage
        para exibir o percentual de codigo que foi testado
    """
    
    def setUp(self):
        pass
    
    def test_posso_setar_permissoes_e_criar_grupo_gestor_com_comando_set_permissions(self):
        call_command('set_permissions')
        group = Group.objects.get(name=settings.GROUPS)
        self.assertTrue(group)
        self.assertTrue(group.permissions.all())
    
    def test_posso_criar_fazenda_e_ver_o_token_dinamico(self):
        fazenda_data = {
            'nome':'teste',
            'cnpj':'teste',
            'telefone':'teste',
            'endereco':'teste',
            # 'access_token':'teste',
        }
        fazenda = Fazenda.objects.create()
        self.assertTrue(fazenda)
        self.assertTrue(fazenda.access_token)

    def test_nao_posso_atualizar_token_da_fazenda(self):
        fazenda_data = {
            'nome':'teste',
            'cnpj':'teste',
            'telefone':'teste',
            'endereco':'teste',
            # 'access_token':'teste',
        }
        fazenda = Fazenda.objects.create()
        self.assertTrue(fazenda)
        self.assertTrue(fazenda.access_token)
        fazenda.access_token = 'outro token'
        fazenda.save()
        fazenda_updated = Fazenda.objects.get(pk=fazenda.pk)
        self.assertEqual(fazenda.access_token, fazenda_updated.access_token)

