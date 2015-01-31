# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('age', models.IntegerField(verbose_name='Idade de uso')),
                ('sickness', models.CharField(max_length=100, verbose_name='Doença')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('start_date', models.DateField(null=True, blank=True, verbose_name='Data de inicio')),
                ('description', models.TextField(blank=True, verbose_name='Descriçao')),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Vacina',
                'verbose_name': 'Vacina',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
