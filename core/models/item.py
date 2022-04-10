from django.db import models
from .lista_compras import ListaCompras

class Item(models.Model):
    '''
    A classe Item serve para armazernar os(as) itens do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Item.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    lista_compras = models.ForeignKey(
        ListaCompras,
        verbose_name="Lista de compras",
        on_delete=models.CASCADE
    )

    concluido = models.BooleanField(
        verbose_name="Concluído",
        default=False,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
