from django.db import models
from django.contrib.auth.models import User

class ListaCompras(models.Model):
    '''
    A classe ListaCompras serve para armazernar os(as) lista de compras do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo ListaCompras.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    proprietario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Lista de Compras'
        verbose_name_plural = 'Listas de Compras'
