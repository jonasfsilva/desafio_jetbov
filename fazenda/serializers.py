import os
from rest_framework import serializers      
from fazenda.models import Fazenda
from fazenda.models import GestorFazenda
from fazenda.models import Gado
from expander import ExpanderSerializerMixin

class FazendaSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):

    __str__ = serializers.SerializerMethodField()

    class Meta:
        model = Fazenda
        fields = (
            
            '__str__',
            'id',
            'nome',
            'cnpj',
            'telefone',
            'endereco',
        )

    def __init__(self, *args, **kwargs):
        super(FazendaSerializer, self).__init__(*args, **kwargs)

    def get___str__(self, obj):
        return obj.__str__()


class GestorFazendaSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    
    __str__ = serializers.SerializerMethodField()

    class Meta:
        model = GestorFazenda
        fields = (
            
            '__str__',
            'id',
            'usuario',
            'fazenda',
        )

    def __init__(self, *args, **kwargs):
        super(GestorFazendaSerializer, self).__init__(*args, **kwargs)

        usuario = self.fields.get('usuario')
        usuario.required = False
        usuario.allow_empty = True
        usuario.allow_null = True

    def get___str__(self, obj):
        return obj.__str__()


class GadoSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):

    __str__ = serializers.SerializerMethodField()

    class Meta:
        model = Gado
        fields = (            
            '__str__',
            'id',
            'numero_brinco',
            'peso',
            'especificacoes',
            'fazenda',
        )

    def __init__(self, *args, **kwargs):
        super(GadoSerializer, self).__init__(*args, **kwargs)

    def get___str__(self, obj):
        return obj.__str__()


f = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "serializers_experts.py")
if os.path.exists(f):
    exec(open(f, "rb").read())