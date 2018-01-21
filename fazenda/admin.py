from django.contrib import admin
from django.contrib.auth.models import Group
from fazenda.models import Fazenda
from fazenda.models import GestorFazenda
from fazenda.models import Gado
from fazenda.models import Pesagem
from django.conf import settings

admin.site.unregister(Group)

@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    
    readonly_fields = ('access_token',)

    def get_queryset(self, request):
        qs = super(FazendaAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gestorfazenda__usuario=request.user)
    
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

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
    """
        Usuario Gestor vê apenas Gado da fazenda que ele é gestor
    """
    
    def get_queryset(self, request):
        qs = super(GadoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(fazenda__gestorfazenda__usuario=request.user)
    
    def has_add_permission(self, request):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_change_permission(self, request, obj=None):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_delete_permission(self, request, obj=None):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

@admin.register(Pesagem)
class PesagemAdmin(admin.ModelAdmin):
    """
        Usuario Gestor vê apenas Pesagens de gado da fazenda que ele é gestor
    """
    
    def get_queryset(self, request):
        qs = super(PesagemAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(gado__fazenda__gestorfazenda__usuario=request.user)
    
    def has_add_permission(self, request):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_change_permission(self, request, obj=None):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser

    def has_delete_permission(self, request, obj=None):
        is_gestor = request.user.groups.filter(name=settings.GROUPS).exists()
        is_superuser = request.user.is_superuser
        return is_gestor or is_superuser