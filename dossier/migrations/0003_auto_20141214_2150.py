# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0002_auto_20141210_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='address',
            field=models.ForeignKey(verbose_name='\u0410\u0434\u0440\u0435\u0441:', to='address.Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dossier',
            name='favorite_color',
            field=models.CharField(blank=True, max_length=6, verbose_name='\u041b\u044e\u0431\u0438\u043c\u044b\u0439 \u0446\u0432\u0435\u0442:', choices=[(b'red', '\u043a\u0440\u0430\u0441\u043d\u044b\u0439'), (b'yellow', '\u0436\u0435\u043b\u0442\u044b\u0439'), (b'blue', '\u0433\u043e\u043b\u0443\u0431\u043e\u0439'), (b'violet', '\u0444\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439'), (b'orange', '\u043e\u0440\u0430\u043d\u0436\u0435\u0432\u044b\u0439'), (b'green', '\u0437\u0435\u043b\u0435\u043d\u044b\u0439'), (b'indigo', '\u0441\u0438\u043d\u0438\u0439')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dossier',
            name='unloved_courses',
            field=models.ManyToManyField(to='courses.Course', verbose_name='\u041d\u0435\u043b\u044e\u0431\u0438\u043c\u044b\u0435 \u043a\u0443\u0440\u0441\u044b:'),
            preserve_default=True,
        ),
    ]
