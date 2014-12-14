# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0004_auto_20141213_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=60, verbose_name='\u0421\u0442\u0440\u0430\u043d\u0430:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(max_length=60, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c:', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='house',
            field=models.CharField(max_length=10, verbose_name='\u0414\u043e\u043c:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='index',
            field=models.PositiveIntegerField(verbose_name='\u0418\u043d\u0434\u0435\u043a\u0441:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(max_length=60, verbose_name='\u0420\u0430\u0439\u043e\u043d:', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=60, verbose_name='\u0423\u043b\u0438\u0446\u0430:'),
            preserve_default=True,
        ),
    ]
