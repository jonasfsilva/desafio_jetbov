"""
    Modificado em 19/01/2018 23:04:21
"""
from rest_framework import serializers
from expander import ExpanderSerializerMixin
from fazenda.serializers import FazendaSerializer
from fazenda.serializers import GestorFazendaSerializer
from fazenda.serializers import GadoSerializer
from fazenda.serializers import GadoSerializer
from fazenda.serializers import GestorFazendaSerializer

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
}
