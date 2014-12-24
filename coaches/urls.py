from django.conf.urls import patterns, include, url
from coaches.views import (CoachCreateView, CoachUpdateView,
                           CoachDeleteView, CoachesListView, CoachDetailView)


urlpatterns = patterns('',
    url(r'^$', CoachesListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', CoachDetailView.as_view(), name='coach-detail'),
    url(r'^create$', CoachCreateView.as_view(), name='coach-create'),
    url(r'^edit/(?P<pk>\d+)/$', CoachUpdateView.as_view(), name='coach-edit'),
    url(r'^delete/(?P<pk>\d+)/$', CoachDeleteView.as_view(),
        name='coach-delete'),
)
