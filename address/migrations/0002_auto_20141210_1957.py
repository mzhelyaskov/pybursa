# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='area',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(max_length=60, blank=True),
            preserve_default=True,
        ),
    ]
