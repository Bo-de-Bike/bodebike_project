# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0005_auto_20150201_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='doenca_protecao',
            field=models.CharField(verbose_name='Trata doença', max_length=100),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='dose',
            field=models.CharField(verbose_name='Dose', max_length=100),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='nome',
            field=models.CharField(verbose_name='Nome', max_length=100),
        ),
    ]
