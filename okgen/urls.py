from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



admin.autodiscover()

#handler404 = 'errors.error404'
#handler500 = 'errors.error500'

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),

                       # okgen_cms
                       (r'^$', include('okgen.okgen.okgen_cms.urls')),
                       url(r'link_clicked/(?P<id>\d+)/$', 'okgen_cms.views.link_clicked', name='cms_link_clicked'),
                       url(r'searched_words/(?P<page>\d+)/$', 'okgen_cms.views.searched_words',
                           name='cms_searched_words'),

                       # okgen_banks
                       # url(r'bankalar/$', 'okgen_banks.views.banks', name='banks_banks'),
                       # url(r'banka/(?P<id>\d+)/$', 'okgen_banks.views.bank', name='banks_bank'),

                       url(r'sayfa^$', include('django.contrib.flatpages.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)

urlpatterns += staticfiles_urlpatterns()