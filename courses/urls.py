from django.conf.urls import patterns, include, url
from courses.views import courses_list, course_item
from courses.views import course_edit, course_delete, course_create


urlpatterns = patterns('',
    url(r'^$', courses_list, name='index'),
    url(r'^(?P<course_id>\d+)$', course_item, name='course-detail'),
    url(r'^create$', course_create, name='course-create'),
    url(r'^edit/(?P<course_id>\d+)/$', course_edit, name='course-edit'),
    url(r'^delete/(?P<course_id>\d+)/$', course_delete, name='course-delete'),
)
