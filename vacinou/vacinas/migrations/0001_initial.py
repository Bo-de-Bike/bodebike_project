# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('idade', models.CharField(max_length=15, verbose_name='Idade de uso')),
            ],
            options={
                'ordering': ['idade'],
                'verbose_name_plural': 'Idade',
                'verbose_name': 'Idade',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('dose', models.CharField(max_length=200, verbose_name='Dose')),
                ('dose_qtd', models.CharField(blank=True, max_length=50, null=True, verbose_name='Quantidade da dose')),
                ('via_administracao', models.CharField(blank=True, max_length=25, null=True, verbose_name='Via de aplicaçao')),
                ('descricao', models.TextField(blank=True, verbose_name='Descriçao')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('image', models.ImageField(upload_to='home/images', blank=True, null=True, verbose_name='Imagem')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'Vacina',
                'verbose_name': 'Vacina',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idade',
            name='id_vacina',
            field=models.ManyToManyField(to='vacinas.Vacina', related_name='id_vacina', verbose_name='id_vacina'),
            preserve_default=True,
        ),
    ]
