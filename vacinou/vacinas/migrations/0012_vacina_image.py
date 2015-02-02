# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacinas', '0011_auto_20150201_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacina',
            name='image',
            field=models.ImageField(blank=True, upload_to='home/images', null=True, verbose_name='Imagem'),
            preserve_default=True,
        ),
    ]
