# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Doença')),
                ('image', models.ImageField(upload_to='home/images', blank=True, null=True, verbose_name='Imagem')),
                ('descricao', models.TextField(verbose_name='Sobre a Doença')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('id_vacina', models.ManyToManyField(to='vacinas.Vacina', related_name='v_doenca', verbose_name='id_vacina')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'Doenças',
                'verbose_name': 'Doença',
            },
            bases=(models.Model,),
        ),
    ]
