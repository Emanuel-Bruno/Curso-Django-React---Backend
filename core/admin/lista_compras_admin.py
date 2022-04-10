from django.contrib import admin

from ..models import ListaCompras


@admin.register(ListaCompras)
class ListaComprasAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'proprietario'
    ]

    search_fields = [
        'id',
        'nome',
        'proprietario'
    ]

    list_filter = [
        'proprietario',
    ]

    autocomplete_fields = [
        'proprietario',
    ]
