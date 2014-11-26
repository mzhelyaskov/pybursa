from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^home$', TemplateView.as_view(template_name='home.html')),
    url(r'^product$', TemplateView.as_view(template_name='product.html')),
    url(r'^products$', TemplateView.as_view(template_name='products.html')),
    url(r'^index$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
)
