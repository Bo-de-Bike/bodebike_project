# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0012_vacina_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='descricao',
            field=models.TextField(verbose_name=b'Descri\xc3\xa7ao', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vacina',
            name='doenca_protecao',
            field=models.CharField(max_length=200, verbose_name=b'Trata doen\xc3\xa7a'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Via de aplica\xc3\xa7ao', blank=True),
            preserve_default=True,
        ),
    ]
