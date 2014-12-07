# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20141207_1720'),
        ('students', '0002_auto_20141206_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, to='courses.Course', null=True),
            preserve_default=True,
        ),
    ]
