from django.conf.urls import patterns, include, url
from students.views import students_list, student_item
from students.views import student_edit, student_delete, student_create


urlpatterns = patterns('',
    url(r'^$', students_list, name='index'),
    url(r'^(?P<student_id>\d+)$', student_item, name='student-detail'),
    url(r'^create$', student_create, name='student-create'),
    url(r'^edit/(?P<student_id>\d+)/$', student_edit, name='student-edit'),
    url(r'^delete/(?P<student_id>\d+)/$', student_delete,
        name='student-delete'),
)
