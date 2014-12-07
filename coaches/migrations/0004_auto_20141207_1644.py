# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_auto_20141207_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='course',
            field=models.ForeignKey(to='courses.Course', blank=True),
            preserve_default=True,
        ),
    ]
