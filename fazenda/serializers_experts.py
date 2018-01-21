"""
    Modificado em 20/01/2018 20:45:43
"""
from rest_framework import serializers
from expander import ExpanderSerializerMixin
from fazenda.serializers import FazendaSerializer
from fazenda.serializers import GestorFazendaSerializer
from fazenda.serializers import GadoSerializer
from fazenda.serializers import PesagemSerializer
from fazenda.serializers import GadoSerializer
from fazenda.serializers import GestorFazendaSerializer
from fazenda.serializers import PesagemSerializer
from jetbov.serializers_user import UserSerializer

FazendaSerializer.Meta.expandable_fields = {
    'gestorfazenda_set': (GestorFazendaSerializer, (), {
        'many': True
    }),
    'gado_set': (GadoSerializer, (), {
        'many': True
    }),
}

GestorFazendaSerializer.Meta.expandable_fields = {
    'usuario': UserSerializer,
    'fazenda': FazendaSerializer,
}

GadoSerializer.Meta.expandable_fields = {
    'fazenda': FazendaSerializer,
    'pesagem_set': (PesagemSerializer, (), {
        'many': True
    }),
}

PesagemSerializer.Meta.expandable_fields = {
    'gado': GadoSerializer,
}
