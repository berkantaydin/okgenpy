from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'okgen_cms.views.landing', name='cms_landing'),
    url(r'^link_clicked$', 'okgen_cms.views.link_clicked', name='cms_link_clicked'),
)
