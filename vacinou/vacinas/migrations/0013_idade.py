# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0012_vacina_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('idade', models.CharField(max_length=15, verbose_name='Idade de uso')),
                ('id_vacina', models.ManyToManyField(related_name='id_vacina', to='vacinas.Vacina', verbose_name='id_vacina')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
