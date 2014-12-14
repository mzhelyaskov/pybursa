# -*- coding: utf-8 -*-

from django.db import models


class Address(models.Model):
    index = models.PositiveIntegerField()
    country = models.CharField(max_length=60)
    district = models.CharField(max_length=60, blank=True)
    region = models.CharField(max_length=60, blank=True)
    street = models.CharField(max_length=60)
    house = models.CharField(max_length=10)

    def __unicode__(self):
        address_pref = u'%s, %s' % (self.index, self.country)
        district = ''
        if self.district:
            district = u', %s обл.' % self.district
        region = ''
        if region:
            region = u', %s р-н' % self.region
        address_suffix = u', ул. %s, д. %s' % (self.street, self.house)
        return address_pref + district + region + address_suffix