# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150202_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade_de_vacinacao',
            name='endereco',
            field=models.CharField(verbose_name='Endereco', max_length=100),
        ),
    ]
