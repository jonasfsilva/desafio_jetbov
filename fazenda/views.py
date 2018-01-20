"""
    Modificado em 19/01/2018 22:19:16
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
from fazenda.models import Fazenda
from fazenda.models import GestorFazenda
from fazenda.models import Gado
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
        }


class FazendaViewSet(viewsets.ModelViewSet):
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
    )

    def list(self, request, *args, **kwargs):
        """Retorna todas os(as) Fazenda"""
        self.serializer_class = FazendaSerializer
        return super(FazendaViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Cadastro de novo(a) Fazenda"""
        return super(FazendaViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retorna um(a) Fazenda pelo id"""
        self.serializer_class = FazendaSerializer
        return super(FazendaViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Atualiza um(a) Fazenda pelo id"""
        return super(FazendaViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Atualiza alguns campos de um(a) Fazenda pelo id"""
        return super(FazendaViewSet, self).partial_update(
            request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Apaga um(a) Fazenda pelo id"""
        return super(FazendaViewSet, self).destroy(request, *args, **kwargs)


class GestorFazendaFilter(filters.FilterSet):

    fazenda = filters.RelatedFilter(
        FazendaFilter, name='fazenda', queryset=Fazenda.objects.all())

    class Meta:
        model = GestorFazenda
        fields = {
            'id': '__all__',
        }


class GestorFazendaViewSet(viewsets.ModelViewSet):
    queryset = GestorFazenda.objects.all()
    serializer_class = GestorFazendaSerializer
    filter_class = GestorFazendaFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ()
    search_fields = ()

    def list(self, request, *args, **kwargs):
        """Retorna todas os(as) GestorFazenda"""
        self.serializer_class = GestorFazendaSerializer
        return super(GestorFazendaViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Cadastro de novo(a) GestorFazenda"""
        return super(GestorFazendaViewSet, self).create(
            request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retorna um(a) GestorFazenda pelo id"""
        self.serializer_class = GestorFazendaSerializer
        return super(GestorFazendaViewSet, self).retrieve(
            request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Atualiza um(a) GestorFazenda pelo id"""
        return super(GestorFazendaViewSet, self).update(
            request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Atualiza alguns campos de um(a) GestorFazenda pelo id"""
        return super(GestorFazendaViewSet, self).partial_update(
            request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Apaga um(a) GestorFazenda pelo id"""
        return super(GestorFazendaViewSet, self).destroy(
            request, *args, **kwargs)


class GadoFilter(filters.FilterSet):

    fazenda = filters.RelatedFilter(
        FazendaFilter, name='fazenda', queryset=Fazenda.objects.all())

    class Meta:
        model = Gado
        fields = {
            'id': '__all__',
            'numero_brinco': '__all__',
            'peso': '__all__',
            'especificacoes': '__all__',
        }


class GadoViewSet(viewsets.ModelViewSet):
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

    def list(self, request, *args, **kwargs):
        """Retorna todas os(as) Gado"""
        self.serializer_class = GadoSerializer
        return super(GadoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Cadastro de novo(a) Gado"""
        return super(GadoViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retorna um(a) Gado pelo id"""
        self.serializer_class = GadoSerializer
        return super(GadoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Atualiza um(a) Gado pelo id"""
        return super(GadoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Atualiza alguns campos de um(a) Gado pelo id"""
        return super(GadoViewSet, self).partial_update(request, *args,
                                                       **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Apaga um(a) Gado pelo id"""
        return super(GadoViewSet, self).destroy(request, *args, **kwargs)
