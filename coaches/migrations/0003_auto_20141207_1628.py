# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_coach_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='BIRTH_DATE',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='COURSE',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='EMAIL',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='NAME',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='PHONE',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='POSITION',
            new_name='position',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='SURNAME',
            new_name='surname',
        ),
    ]
