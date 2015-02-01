# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0007_auto_20150201_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(verbose_name='Quantidade da dose', max_length=50, blank=True),
        ),
    ]
