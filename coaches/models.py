# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Coach(models.Model):
    user = models.ForeignKey(User, verbose_name=_(u"Польз-ь:"),
                             null=True, blank=True)
    name = models.CharField(_(u'Имя:'), max_length=60)
    surname = models.CharField(_(u'Фамилия:'), max_length=60)
    birth_date = models.DateField(_(u'Дата рождения:'),)
    email = models.EmailField()
    phone = models.CharField(_(u'Тел:'), max_length=15)
    lecturer = 'LR'
    assistant = 'AT'
    position_view = (
        (lecturer, _(u'Лектор')),
        (assistant, _(u'Ассистент')),
    )
    role = models.CharField(u'Роль:', max_length=2, choices=position_view,
                            default=lecturer)
    dossier = models.OneToOneField('dossier.Dossier',
                                   verbose_name=_(u"Досье:"),
                                   null=True, blank=True)
    photo = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.surname + ' ' + self.name