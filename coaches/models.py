# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.ForeignKey(User, verbose_name=u"Польз-ь:",)
    name = models.CharField(u'Имя:', max_length=60)
    surname = models.CharField(u'Фамилия:', max_length=60)
    birth_date = models.DateField(u'Дата рождения:',)
    email = models.EmailField()
    phone = models.CharField(u'Тел:', max_length=15)
    lecturer = 'LR'
    assistant = 'AT'
    position_view = (
        (lecturer, 'Lecturer'),
        (assistant, 'Assistant'),
    )
    role = models.CharField(u'Роль:', max_length=2, choices=position_view,
                            default=lecturer)
    dossier = models.OneToOneField('dossier.Dossier', verbose_name=u"Досье:",
                                   null=True, blank=True)

    def __unicode__(self):
        return self.surname + ' ' + self.name