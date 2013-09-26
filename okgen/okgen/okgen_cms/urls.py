from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'okgen_cms.views.landing', name='cms-landing'),
)
