from django.conf.urls import patterns, include, url
from courses.views import (CourseCreateView, CourseUpdateView,
                           CourseDeleteView, CoursesListView, CourseDetailView)


urlpatterns = patterns('',
    url(r'^$', CoursesListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', CourseDetailView.as_view(), name='course-detail'),
    url(r'^create$', CourseCreateView.as_view(), name='course-create'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='course-edit'),
    url(r'^delete/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='course-delete'),
)