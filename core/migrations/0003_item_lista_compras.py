# Generated by Django 3.1.14 on 2022-04-10 02:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lista_compras',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.listacompras', verbose_name='Lista de compras'),
            preserve_default=False,
        ),
    ]
