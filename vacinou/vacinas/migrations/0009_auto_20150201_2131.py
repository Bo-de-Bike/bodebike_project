# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0008_auto_20150201_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(null=True, blank=True, max_length=50, verbose_name='Quantidade da dose'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(null=True, blank=True, max_length=25, verbose_name='Via de aplicaçao'),
        ),
    ]
