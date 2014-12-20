from django.conf.urls import patterns, include, url
from students.views import students_list, student_item, student_edit


urlpatterns = patterns('',
    url(r'^$', students_list, name='index'),
    url(r'^edit/(?P<student_id>\d+)/$', student_edit, name='student-edit'),
    url(r'^(?P<student_id>\d+)$', student_item, name='student-detail'),
)
