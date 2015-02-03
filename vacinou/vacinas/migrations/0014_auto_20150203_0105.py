# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0013_idade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idade',
            options={'verbose_name_plural': 'Idade', 'ordering': ['idade'], 'verbose_name': 'Idade'},
        ),
        migrations.RemoveField(
            model_name='vacina',
            name='idade',
        ),
    ]
