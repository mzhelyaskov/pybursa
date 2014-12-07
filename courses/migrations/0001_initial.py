# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('COURSE_NAME', models.CharField(max_length=60)),
                ('PROGRAMMING_LEN', models.CharField(default=b'PY', max_length=2, choices=[(b'RU', b'Ruby'), (b'PY', b'Python'), (b'JV', b'Java'), (b'JS', b'JavaScript')])),
                ('DESCRIPTION', models.CharField(max_length=255)),
                ('START_DATE', models.DateField()),
                ('END_DATE', models.DateField()),
                ('ASSISTANT', models.ForeignKey(related_name='assistant_id', to='coaches.Coach')),
                ('TEACHER', models.ForeignKey(related_name='teacher_id', to='coaches.Coach')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
