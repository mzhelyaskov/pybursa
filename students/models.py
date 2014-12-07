from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    STANDARD = 'SD'
    GOLD = 'GD'
    VIP = 'VP'
    PACKAGE_VIEW = (
        (STANDARD, 'Standard'),
        (GOLD, 'Gold'),
        (VIP, 'VIP'),
    )
    package = models.CharField(max_length=2, choices=PACKAGE_VIEW,
                               default=STANDARD)
    course = models.ForeignKey('courses.Course')

    def __unicode__(self):
        return self.surname + ' ' + self.name