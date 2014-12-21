# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0013_coach_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='user',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437-\u044c:', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
