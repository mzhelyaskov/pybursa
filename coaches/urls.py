from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coach_item
from coaches.views import coach_edit, coach_delete, coach_create


urlpatterns = patterns('',
    url(r'^$', coaches_list, name='index'),
    url(r'^(?P<coach_id>\d+)$', coach_item, name='coach-detail'),
    url(r'^create$', coach_create, name='coach-create'),
    url(r'^edit/(?P<coach_id>\d+)/$', coach_edit, name='coach-edit'),
    url(r'^delete/(?P<coach_id>\d+)/$', coach_delete, name='coach-delete'),
)
