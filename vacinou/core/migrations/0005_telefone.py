# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150202_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fone', models.CharField(verbose_name='Telefone', blank=True, max_length=30)),
                ('id_unidade', models.ForeignKey(verbose_name='id_unidade', to='core.Unidade_de_Vacinacao', related_name='t_unidade')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
                'ordering': ['fone'],
            },
            bases=(models.Model,),
        ),
    ]
