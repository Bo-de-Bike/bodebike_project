# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0003_auto_20150201_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(verbose_name='Quantidade da dose', blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(verbose_name='Via de aplicaçao', blank=True, max_length=25),
        ),
    ]
