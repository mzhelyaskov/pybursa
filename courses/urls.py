from django.conf.urls import patterns, include, url
from courses.views import courses_list, course_item


urlpatterns = patterns('',
    url(r'^$', courses_list, name='index'),
    url(r'^(?P<course_id>\d+)$', course_item, name='course-detail'),

)
