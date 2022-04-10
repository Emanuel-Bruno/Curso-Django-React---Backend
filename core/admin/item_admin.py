from django.contrib import admin

from ..models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'lista_compras',
        'concluido',
    ]

    search_fields = [
        'id',
        'lista_compras',
    ]

    list_filter = [
        'nome',
    ]

    autocomplete_fields = [
        'lista_compras',
    ]
