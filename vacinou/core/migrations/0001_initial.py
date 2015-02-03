# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fone', models.CharField(max_length=30, verbose_name='Telefone', blank=True)),
            ],
            options={
                'ordering': ['fone'],
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unidade_de_Vacinacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rpa', models.IntegerField(verbose_name='Rpa')),
                ('unidade', models.CharField(max_length=100, verbose_name='Unidade')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereco')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('latitude', models.CharField(max_length=20, verbose_name='latitude', blank=True)),
                ('longitude', models.CharField(max_length=20, verbose_name='longitude', blank=True)),
            ],
            options={
                'ordering': ['unidade'],
                'verbose_name': 'Unidade de Vacinação',
                'verbose_name_plural': 'Unidades de Vacinação',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='telefone',
            name='id_unidade',
            field=models.ForeignKey(verbose_name='id_unidade', to='core.Unidade_de_Vacinacao', related_name='t_unidade'),
            preserve_default=True,
        ),
    ]
