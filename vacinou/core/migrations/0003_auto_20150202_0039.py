# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150202_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade_de_vacinacao',
            name='fone',
            field=models.CharField(verbose_name='Telefone', blank=True, max_length=30),
        ),
    ]
