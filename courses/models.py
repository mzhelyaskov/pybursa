from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=60)
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
    programming_len = models.CharField(max_length=2,
                                       choices=programming_len_view,
                                       default=python)
    description = models.CharField(max_length=255)
    teacher = models.ForeignKey('coaches.Coach',
                                limit_choices_to={'position': 'LR'},
                                related_name='teacher_id')
    assistant = models.ForeignKey('coaches.Coach',
                                  limit_choices_to={'position': 'AT'},
                                  related_name='assistant_id',
                                  null=True,
                                  blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.course_name + ' (' + self.programming_len + ')'