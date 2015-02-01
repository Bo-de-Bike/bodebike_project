# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0010_auto_20150201_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(max_length=50, verbose_name='Quantidade da dose', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(max_length=25, verbose_name='Via de aplicaçao', blank=True, null=True),
        ),
    ]
