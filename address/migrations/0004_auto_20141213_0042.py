# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20141213_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='zcode',
            new_name='index',
        ),
    ]
