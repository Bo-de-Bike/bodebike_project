# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0002_auto_20150201_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacina',
            options={'verbose_name': 'Vacina', 'verbose_name_plural': 'Vacina', 'ordering': ['nome']},
        ),
        migrations.RenameField(
            model_name='vacina',
            old_name='name',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='vacina',
            name='doenca_protecao',
            field=models.CharField(max_length=50, verbose_name='Trata doença'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='dose',
            field=models.CharField(max_length=20, verbose_name='Dose'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(max_length=15, verbose_name='Quantidade da dose'),
        ),
        migrations.AlterField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(max_length=25, verbose_name='Via de aplicaçao'),
        ),
    ]
