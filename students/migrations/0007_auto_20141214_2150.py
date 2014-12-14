# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436-\u044f:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='courses.Course', verbose_name='\u041a\u0443\u0440\u0441\u044b:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='dossier.Dossier', verbose_name='\u0414\u043e\u0441\u044c\u0435:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=60, verbose_name='\u0418\u043c\u044f:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(default=b'SD', max_length=2, verbose_name='\u041f\u0430\u043a\u0435\u0442:', choices=[(b'SD', b'Standard'), (b'GD', b'Gold'), (b'VP', b'VIP')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=60, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f:'),
            preserve_default=True,
        ),
    ]
