# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('package', models.CharField(default=b'SD', max_length=2, choices=[(b'SD', b'Standard'), (b'GD', b'Gold'), (b'VP', b'VIP')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
