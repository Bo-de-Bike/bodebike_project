# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0006_auto_20150201_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='doenca_protecao',
            field=models.CharField(max_length=200, verbose_name='Trata doença'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='dose',
            field=models.CharField(max_length=200, verbose_name='Dose'),
        ),
    ]
