# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0010_auto_20141214_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='birth_date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='dossier.Dossier', verbose_name='\u0414\u043e\u0441\u044c\u0435:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(max_length=60, verbose_name='\u0418\u043c\u044f:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='role',
            field=models.CharField(default=b'LR', max_length=2, verbose_name='\u0420\u043e\u043b\u044c:', choices=[(b'LR', b'Lecturer'), (b'AT', b'Assistant')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='surname',
            field=models.CharField(max_length=60, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='user',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u043b\u044c\u0437-\u044c:', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
