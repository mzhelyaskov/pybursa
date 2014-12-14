# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20141210_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='area',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='index',
            new_name='zcode',
        ),
    ]
