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
        (red, u'Красный'),
        (yellow, u'Желтый'),
        (blue, u'Голубой'),
        (violet, u'Фиолетовый'),
        (orange, u'Оранжевый'),
        (green, u'Зеленый'),
        (indigo, u'Синий'),
    )
    address = models.ForeignKey('address.Address',
                                verbose_name=u"Адрес:")
    unloved_courses = models.ManyToManyField('courses.Course',
                                             verbose_name=u"Нелюбимые курсы:")
    favorite_color = models.CharField(u"Любимый цвет:", max_length=6,
                                      choices=favorite_color_view,
                                      blank=True, null=True)

    def __unicode__(self):
        return u"Досье №%s" % self.id