from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
import rest_framework_filters as filters
from .serializers_user import UserSerializer
from rest_framework.exceptions import APIException
from django.conf import settings


# class UserFilter(filters.FilterSet):
    
#     id = filters.AllLookupsFilter()
#     first_name = filters.AllLookupsFilter()
#     last_name = filters.AllLookupsFilter()
#     username = filters.AllLookupsFilter()
#     email = filters.AllLookupsFilter()

#     class Meta:
#         model = User
        # fields = ['id', 'username']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_class = UserFilter
    filter_backends = (DjangoFilterBackend,)

    def list(self, request, *args, **kwargs):        
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Atualiza um(a) User pelo id"""
        raise APIException(
            "Não é Possivel atualizar Usuarios")

    def partial_update(self, request, *args, **kwargs):
        """Atualiza alguns campos de um(a) User pelo id"""
        raise APIException(
            "Não é Possivel atualizar parcialmente Usuarios")

    def destroy(self, request, *args, **kwargs):
        """Apaga um(a) User pelo id"""
        raise APIException(
            "Não é Possivel deletar usuarios"
        )