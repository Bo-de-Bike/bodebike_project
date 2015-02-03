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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idade', models.CharField(max_length=15, verbose_name='Idade de uso')),
            ],
            options={
                'ordering': ['idade'],
                'verbose_name': 'Idade',
                'verbose_name_plural': 'Idade',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('dose', models.CharField(max_length=200, verbose_name='Dose')),
                ('dose_qtd', models.CharField(max_length=50, verbose_name='Quantidade da dose', blank=True, null=True)),
                ('via_administracao', models.CharField(max_length=25, verbose_name='Via de aplicaçao', blank=True, null=True)),
                ('descricao', models.TextField(verbose_name='Descriçao', blank=True)),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('image', models.ImageField(verbose_name='Imagem', upload_to='home/images', blank=True, null=True)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Vacina',
                'verbose_name_plural': 'Vacina',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idade',
            name='id_vacina',
            field=models.ManyToManyField(verbose_name='id_vacina', related_name='id_vacina', to='vacinas.Vacina'),
            preserve_default=True,
        ),
    ]
