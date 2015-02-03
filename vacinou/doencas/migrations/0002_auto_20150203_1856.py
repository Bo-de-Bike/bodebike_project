# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doencas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doenca',
            name='descricao',
            field=models.TextField(verbose_name=b'Sobre a Doen\xc3\xa7a'),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b'Nome da Doen\xc3\xa7a'),
        ),
    ]
