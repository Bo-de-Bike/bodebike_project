# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0009_auto_20150201_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacina',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descriçao', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacina',
            name='slug',
            field=models.SlugField(verbose_name='Atalho', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(verbose_name='Quantidade da dose', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(verbose_name='Via de aplicaçao', max_length=25, null=True),
        ),
    ]
