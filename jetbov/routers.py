"""
    Modificado em 19/01/2018 22:19:33
"""
from rest_framework import routers
from .views_user import UserViewSet
from fazenda.views import FazendaViewSet
from fazenda.views import GestorFazendaViewSet
from fazenda.views import GadoViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'fazendas', FazendaViewSet)
router.register(r'gestor_fazendas', GestorFazendaViewSet)
router.register(r'gados', GadoViewSet)



