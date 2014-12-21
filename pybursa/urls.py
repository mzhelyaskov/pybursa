from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^results$', TemplateView.as_view(template_name='result.html'),
        name='result-message'),
)
