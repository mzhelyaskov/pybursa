# -*- coding: utf-8 -*-

from django.db import models


class Course(models.Model):
    course_name = models.CharField(u'Наименование:', max_length=60)
    slug = models.SlugField(unique=True)
    ruby = 'RU'
    python = 'PY'
    java = 'JV'
    javascript = 'JS'
    programming_len_view = (
        (ruby, 'Ruby'),
        (python, 'Python'),
        (java, 'Java'),
        (javascript, 'JavaScript'),
    )
    programming_len = models.CharField(u'Язык программ-я:', max_length=2,
                                       choices=programming_len_view,
                                       default=python)
    description = models.CharField(u'Описание:', max_length=255)
    teacher = models.ForeignKey('coaches.Coach',
                                verbose_name=u"Преподаватель:",
                                limit_choices_to={'role': 'LR'},
                                related_name='teacher_id')
    assistant = models.ForeignKey('coaches.Coach',
                                  verbose_name=u"Ассистент:",
                                  limit_choices_to={'role': 'AT'},
                                  related_name='assistant_id',
                                  null=True,
                                  blank=True)
    start_date = models.DateField(u'Начало:')
    end_date = models.DateField(u'Окончание:')
    venue = models.ForeignKey('address.Address', null=True, blank=True)

    def __unicode__(self):
        return self.course_name + ' (' + self.programming_len + ')'