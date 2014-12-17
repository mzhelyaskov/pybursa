# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0011_auto_20141214_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='role',
            field=models.CharField(default=b'LR', max_length=2, verbose_name='\u0420\u043e\u043b\u044c:', choices=[(b'LR', '\u041b\u0435\u043a\u0442\u043e\u0440'), (b'AT', '\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442')]),
            preserve_default=True,
        ),
    ]
