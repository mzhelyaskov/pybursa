# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NAME', models.CharField(max_length=60)),
                ('SURNAME', models.CharField(max_length=60)),
                ('BIRTH_DATE', models.DateField()),
                ('EMAIL', models.EmailField(max_length=75)),
                ('PHONE', models.CharField(max_length=15)),
                ('POSITION', models.CharField(default=b'LR', max_length=2, choices=[(b'LR', b'Lecturer'), (b'AT', b'Assistant')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
