# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0004_auto_20150201_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='dose',
            field=models.CharField(max_length=50, verbose_name='Dose'),
        ),
    ]
