# -*- coding: utf-8 -*-

from django.db import models


class Student(models.Model):
    name = models.CharField(u'Имя:', max_length=60)
    surname = models.CharField(u'Фамилия:', max_length=60)
    birth_date = models.DateField(u'Дата рож-я:',)
    email = models.EmailField()
    phone = models.CharField(u'Тел:', max_length=15)
    STANDARD = 'SD'
    GOLD = 'GD'
    VIP = 'VP'
    PACKAGE_VIEW = (
        (STANDARD, 'Standard'),
        (GOLD, 'Gold'),
        (VIP, 'VIP'),
    )
    package = models.CharField(u'Пакет:', max_length=2, choices=PACKAGE_VIEW,
                               default=STANDARD)
    courses = models.ManyToManyField('courses.Course', verbose_name=u"Курсы:",)
    dossier = models.OneToOneField('dossier.Dossier', verbose_name=u"Досье:",
                                   null=True, blank=True)
    photo = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.surname + ' ' + self.name