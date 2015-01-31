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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Doença')),
                ('image', models.ImageField(upload_to='home/images', blank=True, null=True, verbose_name='Imagem')),
                ('descricao', models.TextField(verbose_name='Sobre a Doença')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('id_vacina', models.ForeignKey(related_name='v_doenca', verbose_name='id_vacina', to='vacinas.Vacina')),
            ],
            options={
                'verbose_name_plural': 'Doenças',
                'verbose_name': 'Doença',
                'ordering': ['nome'],
            },
            bases=(models.Model,),
        ),
    ]
