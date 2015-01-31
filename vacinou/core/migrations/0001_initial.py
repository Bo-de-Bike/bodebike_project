# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unidade_de_Vacinacao',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('endereco', models.CharField(max_length=400, verbose_name='Endereço')),
                ('unidade', models.CharField(max_length=100, verbose_name='Unidade')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('fone', models.CharField(blank=True, max_length=14, verbose_name='Telefone')),
                ('latitude', models.CharField(blank=True, max_length=20, verbose_name='latitude')),
                ('longitude', models.CharField(blank=True, max_length=20, verbose_name='longitude')),
                ('slug', models.SlugField(verbose_name='Atalho')),
            ],
            options={
                'verbose_name_plural': 'Unidades de Vacinação',
                'verbose_name': 'Unidade de Vacinação',
                'ordering': ['unidade'],
            },
            bases=(models.Model,),
        ),
    ]
