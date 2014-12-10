# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0007_coach_dossier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='position',
            new_name='role',
        ),
    ]
