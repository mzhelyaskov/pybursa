# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=60, verbose_name=b'Course:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
