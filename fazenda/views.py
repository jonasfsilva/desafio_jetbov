"""
    Modificado em 20/01/2018 20:45:29
"""
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
import rest_framework_filters as filters
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from fazenda.serializers import FazendaSerializer
from fazenda.serializers import GestorFazendaSerializer
from fazenda.serializers import GadoSerializer
from fazenda.serializers import PesagemSerializer
from fazenda.models import Fazenda
from fazenda.models import GestorFazenda
from fazenda.models import Gado
from fazenda.models import Pesagem
from django.contrib.auth.models import User
# from jetbov.views_user import UserFilter


class FazendaFilter(filters.FilterSet):
    class Meta:
        model = Fazenda
        fields = {
            'id': '__all__',
            'nome': '__all__',
            'cnpj': '__all__',
            'telefone': '__all__',
            'endereco': '__all__',
            'access_token': '__all__',
        }


class FazendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializer
    filter_class = FazendaFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = (
        'nome',
        'cnpj',
        'telefone',
        'endereco',
    )
    search_fields = (
        'nome',
        'cnpj',
        'telefone',
        'endereco',
        # 'access_token',
    )


class GestorFazendaFilter(filters.FilterSet):

    fazenda = filters.RelatedFilter(
        FazendaFilter, name='fazenda', queryset=Fazenda.objects.all())

    class Meta:
        model = GestorFazenda
        fields = {
            'id': '__all__',
        }


class GestorFazendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GestorFazenda.objects.all()
    serializer_class = GestorFazendaSerializer
    filter_class = GestorFazendaFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ()
    search_fields = ()

    
class GadoFilter(filters.FilterSet):

    fazenda = filters.RelatedFilter(
        FazendaFilter, name='fazenda', queryset=Fazenda.objects.all())

    class Meta:
        model = Gado
        fields = {
            'id': '__all__',
            'numero_brinco': '__all__',
            'especificacoes': '__all__',
        }


class GadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Gado.objects.all()
    serializer_class = GadoSerializer
    filter_class = GadoFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = (
        'numero_brinco',
        'especificacoes',
    )
    search_fields = (
        'numero_brinco',
        'especificacoes',
    )


class PesagemFilter(filters.FilterSet):

    gado = filters.RelatedFilter(
        GadoFilter, name='gado', queryset=Gado.objects.all())

    class Meta:
        model = Pesagem
        fields = {
            'id': '__all__',
            'peso': '__all__',
            'data_pesagem': '__all__',
        }


class PesagemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pesagem.objects.all()
    serializer_class = PesagemSerializer
    filter_class = PesagemFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('data_pesagem', )
    search_fields = ('data_pesagem', )
