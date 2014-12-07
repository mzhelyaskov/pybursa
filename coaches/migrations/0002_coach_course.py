# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='COURSE',
            field=models.ForeignKey(to='courses.Course'),
            preserve_default=True,
        ),
    ]
