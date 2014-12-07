from django.conf.urls import patterns, include, url
from coaches.views import coaches_list, coach_item


urlpatterns = patterns('',
    url(r'^$', coaches_list),
    url(r'^(?P<student_id>\d+)$', coach_item),

)
