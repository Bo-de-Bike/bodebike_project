# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0014_auto_20150203_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacina',
            name='doenca_protecao',
        ),
    ]
