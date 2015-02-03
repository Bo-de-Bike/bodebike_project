# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidade_de_vacinacao',
            name='fone',
        ),
    ]
