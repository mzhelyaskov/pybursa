# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0004_course_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorite_color', models.CharField(blank=True, max_length=6, choices=[(b'red', b'\xd0\xba\xd1\x80\xd0\xb0\xd1\x81\xd0\xbd\xd1\x8b\xd0\xb9'), (b'yellow', b'\xd0\xb6\xd0\xb5\xd0\xbb\xd1\x82\xd1\x8b\xd0\xb9'), (b'blue', b'\xd0\xb3\xd0\xbe\xd0\xbb\xd1\x83\xd0\xb1\xd0\xbe\xd0\xb9'), (b'violet', b'\xd1\x84\xd0\xb8\xd0\xbe\xd0\xbb\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9'), (b'orange', b'\xd0\xbe\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb6\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb9'), (b'green', b'\xd0\xb7\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd1\x8b\xd0\xb9'), (b'indigo', b'\xd1\x81\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xb9')])),
                ('address', models.ForeignKey(to='address.Address')),
                ('unloved_courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
