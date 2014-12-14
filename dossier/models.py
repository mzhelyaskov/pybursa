# -*- coding: utf-8 -*-

from django.db import models


class Dossier(models.Model):
    red = 'red'
    yellow = 'yellow'
    blue = 'blue'
    violet = 'violet'
    orange = 'orange'
    green = 'green'
    indigo = 'indigo'
    favorite_color_view = (
        (red, u'красный'),
        (yellow, u'желтый'),
        (blue, u'голубой'),
        (violet, u'фиолетовый'),
        (orange, u'оранжевый'),
        (green, u'зеленый'),
        (indigo, u'синий'),
    )
    address = models.ForeignKey('address.Address')
    unloved_courses = models.ManyToManyField('courses.Course')
    favorite_color = models.CharField(max_length=6,
                                      choices=favorite_color_view,
                                      blank=True)

    def __unicode__(self):
        return u"Досье №%s" % self.id