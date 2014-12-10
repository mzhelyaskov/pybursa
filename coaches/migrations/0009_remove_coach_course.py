# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0008_auto_20141210_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='course',
        ),
    ]
