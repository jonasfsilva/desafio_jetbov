from django.contrib import admin
from fazenda.models import Fazenda
from fazenda.models import GestorFazenda
from fazenda.models import Gado


@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    pass


@admin.register(GestorFazenda)
class GestorFazendaAdmin(admin.ModelAdmin):
    pass


@admin.register(Gado)
class GadoAdmin(admin.ModelAdmin):
    pass
