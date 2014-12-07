# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='ASSISTANT',
            new_name='assistant',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='COURSE_NAME',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='DESCRIPTION',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='END_DATE',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='PROGRAMMING_LEN',
            new_name='programming_len',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='START_DATE',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='TEACHER',
            new_name='teacher',
        ),
    ]
