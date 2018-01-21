from django.contrib import admin
from fazenda.models import Fazenda
from fazenda.models import GestorFazenda
from fazenda.models import Gado
from fazenda.models import Pesagem


@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(GestorFazenda)
class GestorFazendaAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(Gado)
class GadoAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        is_gestor = hasattr(request.user, 'gestorfazenda')
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_change_permission(self, request, obj=None):
        is_gestor = hasattr(request.user, 'gestorfazenda')
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_delete_permission(self, request, obj=None):
        is_gestor = hasattr(request.user, 'gestorfazenda')
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

@admin.register(Pesagem)
class PesagemAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        is_gestor = hasattr(request.user, 'gestorfazenda')
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_change_permission(self, request, obj=None):
        is_gestor = hasattr(request.user, 'gestorfazenda')
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_delete_permission(self, request, obj=None):
        is_gestor = hasattr(request.user, 'gestorfazenda')
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser