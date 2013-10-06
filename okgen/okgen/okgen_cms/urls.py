from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'okgen_cms.views.landing', name='cms_landing'),
                       url(r'link_clicked/(?P<id>\d+)/$', 'okgen_cms.views.link_clicked', name='cms_link_clicked'),
                       url(r'searched_words/(?P<page>[\d-]*)/$', 'okgen_cms.views.searched_words',
                           name='cms_searched_words'),
                       url(r'^links/(?P<slug>[\w-]+)/$', 'okgen_cms.views.links', name='cms_links'),
)
