# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20141213_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant_id', verbose_name='\u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442:', blank=True, to='coaches.Coach', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=60, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=255, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='programming_len',
            field=models.CharField(default=b'PY', max_length=2, verbose_name='\u042f\u0437\u044b\u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c-\u044f:', choices=[(b'RU', b'Ruby'), (b'PY', b'Python'), (b'JV', b'Java'), (b'JS', b'JavaScript')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_name='teacher_id', verbose_name='\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c:', to='coaches.Coach'),
            preserve_default=True,
        ),
    ]
