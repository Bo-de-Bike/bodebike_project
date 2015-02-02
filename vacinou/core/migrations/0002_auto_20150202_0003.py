# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidade_de_vacinacao',
            name='slug',
        ),
        migrations.AddField(
            model_name='unidade_de_vacinacao',
            name='rpa',
            field=models.IntegerField(default=1, verbose_name='Rpa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unidade_de_vacinacao',
            name='endereco',
            field=models.CharField(max_length=100, verbose_name='Unidade'),
        ),
    ]
