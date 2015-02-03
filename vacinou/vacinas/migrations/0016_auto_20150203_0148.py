# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0015_remove_vacina_doenca_protecao'),
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
            name='via_administracao',
            field=models.CharField(max_length=25, null=True, verbose_name=b'Via de aplica\xc3\xa7ao', blank=True),
            preserve_default=True,
        ),
    ]
