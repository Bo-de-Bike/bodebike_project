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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Doença')),
                ('image', models.ImageField(verbose_name='Imagem', upload_to='home/images', blank=True, null=True)),
                ('descricao', models.TextField(verbose_name='Sobre a Doença')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('id_vacina', models.ManyToManyField(verbose_name='id_vacina', related_name='v_doenca', to='vacinas.Vacina')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Doença',
                'verbose_name_plural': 'Doenças',
            },
            bases=(models.Model,),
        ),
    ]
