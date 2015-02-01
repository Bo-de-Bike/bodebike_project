# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacina',
            name='age',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='description',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='sickness',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='vacina',
            name='doenca_protecao',
            field=models.CharField(verbose_name='Doença', max_length=50, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacina',
            name='dose',
            field=models.CharField(verbose_name='Doença', max_length=20, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacina',
            name='dose_qtd',
            field=models.CharField(verbose_name='Doença', max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacina',
            name='idade',
            field=models.CharField(verbose_name='Idade de uso', max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacina',
            name='via_administracao',
            field=models.CharField(verbose_name='Doença', max_length=25, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacina',
            name='name',
            field=models.CharField(verbose_name='Nome', max_length=50),
        ),
    ]
