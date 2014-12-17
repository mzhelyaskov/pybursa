# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_auto_20141214_2150'),
        ('students', '0007_auto_20141214_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.ForeignKey(blank=True, to='address.Address', null=True),
            preserve_default=True,
        ),
    ]
