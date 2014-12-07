# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_auto_20141207_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='course',
            field=models.ForeignKey(blank=True, to='courses.Course', null=True),
            preserve_default=True,
        ),
    ]
