from django.db import models
from pybursa import settings


class Coach(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    lecturer = 'LR'
    assistant = 'AT'
    position_view = (
        (lecturer, 'Lecturer'),
        (assistant, 'Assistant'),
    )
    role = models.CharField(max_length=2, choices=position_view,
                            default=lecturer)
    dossier = models.OneToOneField('dossier.Dossier', null=True, blank=True)

    def __unicode__(self):
        return self.surname + ' ' + self.name